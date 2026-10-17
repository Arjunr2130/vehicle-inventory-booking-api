from datetime import date
from decimal import Decimal
from django.db import transaction
from django.db.models import Q
from rest_framework import viewsets, generics, serializers
from rest_framework.exceptions import ValidationError
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by('id')
    serializer_class = VehicleSerializer
    filterset_fields = ['brand', 'fuel_type', 'is_available']


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.select_related('vehicle').all().order_by('-id')
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            vehicle_id = serializer.validated_data['vehicle'].id

            # Lock the vehicle while checking and creating a booking.
            vehicle = Vehicle.objects.select_for_update().get(
                id=vehicle_id
            )

            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']

            if start_date < date.today():
                raise ValidationError({
                    'start_date': 'Start date cannot be in the past.'
                })

            if end_date <= start_date:
                raise ValidationError({
                    'end_date': 'End date must be after start date.'
                })

            # Check for overlapping booking dates.
            overlapping_booking = Booking.objects.filter(
                vehicle=vehicle,
                start_date__lt=end_date,
                end_date__gt=start_date
            ).exists()

            if overlapping_booking:
                raise ValidationError({
                    'vehicle': 'This vehicle is already booked for these dates.'
                })

            if not vehicle.is_available:
                raise ValidationError({
                    'vehicle': 'This vehicle is currently unavailable.'
                })

            days = (end_date - start_date).days
            total_amount = Decimal(days) * vehicle.price_per_day

            serializer.save(
                vehicle=vehicle,
                total_amount=total_amount
            )

            vehicle.is_available = False
            vehicle.save(update_fields=['is_available'])


class BookingRetrieveView(generics.RetrieveAPIView):
    queryset = Booking.objects.select_related('vehicle').all()
    serializer_class = BookingSerializer
