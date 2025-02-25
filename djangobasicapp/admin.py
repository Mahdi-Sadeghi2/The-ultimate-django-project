from django.contrib import admin

from .models import Employee, Country, Department, UserRegistration
# Register your models here.


admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(UserRegistration)