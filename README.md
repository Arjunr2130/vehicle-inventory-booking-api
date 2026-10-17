
# Vehicle Inventory & Booking API

A REST API built using Django and Django REST Framework to manage vehicle inventory and vehicle bookings.

## Features

- Create, view, update, and delete vehicles.
- List and create vehicle bookings.
- Retrieve individual booking details.
- Filter vehicles by brand, fuel type, and availability.
- Validate customer phone numbers and booking dates.
- Prevent overlapping bookings for the same vehicle.
- Automatically calculate the total booking amount based on the number of days and the vehicle's daily price.
- Update vehicle availability after a successful booking.
- Interactive API documentation using Swagger UI.

## Technologies Used

- Python
- Django
- Django REST Framework
- Django Filter
- drf-spectacular
- SQLite

## Project Setup

### 1. Clone the Repository

Replace the URL below with your GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd vehicle_booking_project
```

### 2. Create and Activate the Virtual Environment

```powershell
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory using `.env.example` as a reference.

Add your own development secret key and environment settings to `.env`.

Do not upload your actual `.env` file or secret key to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:

http://127.0.0.1:8000/

## API Endpoints

### Vehicle Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/vehicles/` | List all vehicles |
| POST | `/api/vehicles/` | Create a vehicle |
| GET | `/api/vehicles/<id>/` | Retrieve a vehicle |
| PUT | `/api/vehicles/<id>/` | Update a vehicle |
| PATCH | `/api/vehicles/<id>/` | Partially update a vehicle |
| DELETE | `/api/vehicles/<id>/` | Delete a vehicle |

### Booking Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a booking |
| GET | `/api/bookings/<id>/` | Retrieve a booking |

## Vehicle Filters

Vehicles can be filtered using query parameters.

Examples:

```text
/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Petrol
/api/vehicles/?is_available=True
```

## Sample Vehicle Request

Use the following JSON when creating a vehicle:

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

## Sample Booking Request

Use valid future dates when creating a booking.

```json
{
  "vehicle": 1,
  "customer_name": "Arun Kumar",
  "customer_phone": "9876543210",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD"
}
```

Replace `YYYY-MM-DD` with actual dates. The end date must be later than the start date, and the start date cannot be in the past.

The total amount is calculated automatically by the API.

## API Documentation

Swagger UI:

http://127.0.0.1:8000/api/docs/

Use Swagger UI to explore and test the available endpoints.

## Running Tests

Run the automated tests using:

```bash
python manage.py test inventory
```

## Database

The project uses SQLite for local development.

## Deployment

**Hosted API URL:** Add your deployed API URL here after deployment.

## Demo Video

**Demo Video Link:** Add your shareable screen-recording link here after recording the project demonstration.
