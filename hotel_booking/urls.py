from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hotel_booking.views import api_root 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'), 
    path('api/accounts/', include(('accounts.urls', 'accounts'), namespace='accounts-root')),
    path('api/hotels/', include(('hotels.urls', 'hotels'), namespace='hotels-root')),
    path('api/bookings/', include(('bookings.urls', 'bookings'), namespace='bookings-root')),
    path('api/dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard-root')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
