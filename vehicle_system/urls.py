from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from inventory.views import (
    VehicleViewSet,
    BookingListCreateView,
    BookingRetrieveView,
)

router = DefaultRouter()
router.register('vehicles', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path(
        'api/bookings/',
        BookingListCreateView.as_view(),
        name='booking-list-create',
    ),
    path(
        'api/bookings/<int:pk>/',
        BookingRetrieveView.as_view(),
        name='booking-detail',
    ),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]
