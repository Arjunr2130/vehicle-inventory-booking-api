from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Vehicle, Booking


class VehicleBookingAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.vehicle = Vehicle.objects.create(
            name="City",
            brand="Honda",
            year=2024,
            price_per_day=Decimal("2000.00"),
            fuel_type="Petrol",
            is_available=True
        )

    def test_vehicle_list(self):
        response = self.client.get("/api/vehicles/")
        self.assertEqual(response.status_code, 200)

    def test_create_vehicle(self):
        data = {
            "name": "Swift",
            "brand": "Maruti",
            "year": 2023,
            "price_per_day": "1500.00",
            "fuel_type": "Petrol",
            "is_available": True
        }

        response = self.client.post(
            "/api/vehicles/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

    def test_negative_vehicle_price(self):
        data = {
            "name": "Test Car",
            "brand": "Toyota",
            "year": 2024,
            "price_per_day": "-500.00",
            "fuel_type": "Petrol",
            "is_available": True
        }

        response = self.client.post(
            "/api/vehicles/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_create_booking(self):
        start = date.today() + timedelta(days=5)
        end = start + timedelta(days=3)

        data = {
            "vehicle": self.vehicle.id,
            "customer_name": "Arjun",
            "customer_phone": "9876543210",
            "start_date": start.isoformat(),
            "end_date": end.isoformat()
        }

        response = self.client.post(
            "/api/bookings/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

        booking = Booking.objects.get()
        self.assertEqual(booking.total_amount, Decimal("6000.00"))

    def test_invalid_phone_number(self):
        start = date.today() + timedelta(days=5)
        end = start + timedelta(days=2)

        data = {
            "vehicle": self.vehicle.id,
            "customer_name": "Arjun",
            "customer_phone": "123",
            "start_date": start.isoformat(),
            "end_date": end.isoformat()
        }

        response = self.client.post(
            "/api/bookings/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_vehicle_becomes_unavailable_after_booking(self):
        start = date.today() + timedelta(days=5)
        end = start + timedelta(days=2)

        data = {
            "vehicle": self.vehicle.id,
            "customer_name": "Arjun",
            "customer_phone": "9876543210",
            "start_date": start.isoformat(),
            "end_date": end.isoformat()
        }

        response = self.client.post(
            "/api/bookings/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

        self.vehicle.refresh_from_db()
        self.assertFalse(self.vehicle.is_available)