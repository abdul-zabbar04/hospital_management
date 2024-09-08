from django.contrib import admin
from .models import AvailableTime, Designation, Specialization, Doctor, Review

# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
class SpacializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(AvailableTime)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpacializationAdmin)
admin.site.register(Doctor)
admin.site.register(Review)