from django.contrib import admin
from .models import*
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'duration', 'fee')
admin.site.register(Course,CourseAdmin)

class RegistrationAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'course', 'application_form')
admin.site.register(Registration,RegistrationAdmin)
