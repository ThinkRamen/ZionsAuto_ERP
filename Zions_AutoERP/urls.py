from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from vehicles.views import home, vehicles_list, location


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("appointments/", include("appointments.urls")),
    path("vehicles/", vehicles_list, name="vehicles"),
    path("location/", location, name="location"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.index_title = "Site Admin"
admin.site.site_header = "Zions Auto Admin"
admin.site.site_title = "Zions Auto"
