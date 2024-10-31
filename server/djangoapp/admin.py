# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel
class CarModelInline(admin.TabularInline):  # Use TabularInline or StackedInline
    model = CarModel
    extra = 1  # Number of empty forms to display

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Customize fields to display in admin
    search_fields = ('name', 'car_make__name')  # Enable searching by car model name and make

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Customize fields to display in admin
    search_fields = ('name',)  # Enable searching by car make name
    inlines = [CarModelInline]  # Add inline functionality for CarModel

# Register models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
