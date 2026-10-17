from datetime import date
from rest_framework import serializers
from .models import Vehicle, Booking

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

    def validate_year(self, value):
        if value < 1886 or value > date.today().year + 1:
            raise serializers.ValidationError(
                "Enter a valid vehicle manufacturing year."
            )
        return value

    def validate_price_per_day(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price per day must be greater than zero."
            )
        return value


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_amount']

    def validate_customer_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )
        return value

    def validate(self, data):
        start_date = data.get(
            'start_date',
            getattr(self.instance, 'start_date', None)
        )
        end_date = data.get(
            'end_date',
            getattr(self.instance, 'end_date', None)
        )

        if start_date and start_date < date.today():
            raise serializers.ValidationError({
                'start_date': 'Start date cannot be in the past.'
            })

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError({
                'end_date': 'End date must be after start date.'
            })

        return data