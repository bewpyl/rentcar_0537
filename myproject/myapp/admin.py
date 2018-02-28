from django.contrib import admin
from myapp.models import Rent,Car,Return,Person

# Register your models here.


class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
admin.site.register(Rent,RentAdmin)

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]
admin.site.register(Person,PersonAdmin)

class ReturnAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Return._meta.fields]
admin.site.register(Return,ReturnAdmin)
