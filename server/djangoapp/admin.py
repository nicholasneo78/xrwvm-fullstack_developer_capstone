from django.contrib import admin
# Register your models here.
from .models import CarMake, CarModel

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
