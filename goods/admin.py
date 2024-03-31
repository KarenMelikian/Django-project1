from django.contrib import admin

from .models import (Categories,
                     Products_kitchen,
                     Products_bedroom,
                     Products_livingroom,
                     Products_office,
                     Products_accessories,
                     Products_decor)


admin.site.register(Categories)
admin.site.register(Products_kitchen)
admin.site.register(Products_bedroom)
admin.site.register(Products_livingroom)
admin.site.register(Products_office)
admin.site.register(Products_accessories)
admin.site.register(Products_decor)