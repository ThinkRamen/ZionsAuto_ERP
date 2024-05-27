from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from vehicles.views import home, vehicles_list, add_vehicle_by_vin, index


urlpatterns = [
    path("", home, name="home"),
    path("index/", index, name="index"),
    path("admin/", admin.site.urls),
    path("vehicles/", include("vehicles.urls")),
    path("appointments/", include("appointments.urls")),
    path("locations/", include("locations.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.index_title = "Site Admin"
admin.site.site_header = "Zions Auto Admin"
admin.site.site_title = "Zions Auto"
