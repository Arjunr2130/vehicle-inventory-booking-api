
# Vehicle Inventory & Booking API

A REST API built using Django REST Framework to manage vehicle inventory and customer bookings. The API supports vehicle CRUD operations, booking management, input validation, pricing calculations, vehicle filtering, and interactive API documentation.

## Live Demo

- **Live API Documentation (Swagger):**
  https://vehicle-inventory-booking-api-jy1v.onrender.com/api/docs/

- **Vehicles API:**
  https://vehicle-inventory-booking-api-jy1v.onrender.com/api/vehicles/

- **Bookings API:**
  https://vehicle-inventory-booking-api-jy1v.onrender.com/api/bookings/

## Features

- Create, retrieve, update, and delete vehicles.
- List and retrieve individual bookings.
- Filter vehicles by brand, fuel type, and availability.
- Validate vehicle details, customer phone numbers, and booking dates.
- Prevent overlapping bookings for the same vehicle.
- Automatically calculate booking amounts using the daily rental price and booking duration.
- Update vehicle availability after a successful booking.
- Interactive API documentation using Swagger UI.
- Automated tests for API functionality and validation.

## Technologies Used

- Python
- Django
- Django REST Framework
- django-filter
- drf-spectacular
- SQLite for local development
- PostgreSQL for production deployment
- Gunicorn
- Render

## Project Structure

```text
vehicle_system/
├── inventory/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Arjunr2130/vehicle-inventory-booking-api.git
cd vehicle-inventory-booking-api
```

Navigate into the directory containing `manage.py` if your repository has an additional nested project folder.

### 2. Create and Activate a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root, using `.env.example` as a reference.

Configure your local development settings, including a Django secret key and debug mode.

Do not commit your actual `.env` file or production credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

If you have changed your models and created new model fields, generate migrations first:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The local API will be available at:

http://127.0.0.1:8000/

## API Endpoints

### Vehicle Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/vehicles/` | List all vehicles |
| POST | `/api/vehicles/` | Create a vehicle |
| GET | `/api/vehicles/<id>/` | Retrieve vehicle details |
| PUT | `/api/vehicles/<id>/` | Update a vehicle |
| DELETE | `/api/vehicles/<id>/` | Delete a vehicle |

### Booking Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a booking |
| GET | `/api/bookings/<id>/` | Retrieve booking details |

## Vehicle Filtering

Vehicles can be filtered using query parameters.

Examples:

```text
/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Electric
/api/vehicles/?is_available=true
```

## Sample Vehicle Request

Send a POST request to `/api/vehicles/`:

```json
{
  "name": "City",
  "brand": "Honda",
  "year": 2024,
  "price_per_day": "2000.00",
  "fuel_type": "Petrol",
  "is_available": true
}
```

Use a supported fuel type: `Petrol`, `Diesel`, `Electric`, or `Hybrid`.

## Sample Booking Request

Send a POST request to `/api/bookings/`:

```json
{
  "vehicle": 1,
  "customer_name": "Arun Kumar",
  "customer_phone": "9876543210",
  "start_date": "2026-10-20",
  "end_date": "2026-10-22"
}
```

Replace the vehicle ID with an existing vehicle ID and use valid future dates.

The API calculates `total_amount` automatically. The supplied dates are examples; use dates that are valid when you test the API.

## Booking Validation Rules

- Booking start date cannot be in the past.
- Booking end date must be after the start date.
- Customer phone number must contain exactly 10 digits.
- The same vehicle cannot have overlapping bookings.
- Booking amount is calculated automatically using the daily rental price and booking duration.
- Vehicle availability is updated after a successful booking.

Invalid requests should return appropriate validation errors.

## API Documentation

### Swagger UI

Local:

http://127.0.0.1:8000/api/docs/

Production:

https://vehicle-inventory-booking-api-jy1v.onrender.com/api/docs/

Use Swagger UI to explore endpoints, submit requests, inspect responses, and test validation rules.

## Running Tests

Run the automated tests from the directory containing `manage.py`:

```bash
python manage.py test inventory
```

Run Django's system checks:

```bash
python manage.py check
```

## Database Configuration

- **Local development:** SQLite
- **Production deployment:** PostgreSQL on Render

Production database credentials and secret keys are configured using Render environment variables. Do not publish real credentials in this repository.

## Deployment

The API is deployed on Render.

- **Live API Base URL:** https://vehicle-inventory-booking-api-jy1v.onrender.com
- **Swagger API Documentation:** https://vehicle-inventory-booking-api-jy1v.onrender.com/api/docs/
- **Vehicles Endpoint:** https://vehicle-inventory-booking-api-jy1v.onrender.com/api/vehicles/
- **Bookings Endpoint:** https://vehicle-inventory-booking-api-jy1v.onrender.com/api/bookings/

Use the Swagger documentation to test the API endpoints,create bookings, and verify validation rules.

The deployed service uses Gunicorn to run Django and applies database migrations during the build process.

Note: Render free services may take some time to respond after periods of inactivity.

## Demo Video

**Demo Video Link:** Add your shareable Google Drive or YouTube recording link here.

The 2–5 minute demonstration should show:

1. Running or accessing the application.
2. Testing vehicle endpoints in Swagger UI.
3. Creating a booking and verifying the calculated amount.
4. Testing booking validations, including invalid dates and overlapping bookings.
5. Demonstrating vehicle filtering.

## Author

**Arjun R.**
