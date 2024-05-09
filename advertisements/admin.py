from django.contrib import admin
from .models import FacebookAd, OfferUpAd


class FacebookAdAdmin(admin.ModelAdmin):
    readonly_fields = ("title",)  # Specify the title field as read-only


class OfferUpAdAdmin(admin.ModelAdmin):
    readonly_fields = ("title",)  # Specify the title field as read-only


# Register FacebookAd model with FacebookAdAdmin
admin.site.register(FacebookAd, FacebookAdAdmin)

# Register OfferUpAd model with OfferUpAdAdmin
admin.site.register(OfferUpAd, OfferUpAdAdmin)
