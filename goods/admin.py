from django.contrib import admin

from .models import (Categories,
                     ProductsKitchen,
                     ProductsBedroom,
                     ProductsLivingRoom,
                     ProductsOffice,
                     ProductsAccessories,
                     ProductsDecor)


admin.site.register(Categories)
admin.site.register(ProductsKitchen)
admin.site.register(ProductsBedroom)
admin.site.register(ProductsLivingRoom)
admin.site.register(ProductsOffice)
admin.site.register(ProductsAccessories)
admin.site.register(ProductsDecor)