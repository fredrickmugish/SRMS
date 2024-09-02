from django.contrib import admin
from .models import*
from django.utils.html import format_html
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'fee')
    search_fields = ('title', 'duration', 'fee')  
admin.site.register(Course, CourseAdmin)

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1  

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'course', 'view_application_form')
    search_fields = ('last_name', 'course__title') 
    inlines = [PaymentInline] 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def view_application_form(self, obj):
        if obj.application_form:
            return format_html('<a href="{}" target="_blank">View Form</a>', obj.application_form.url)
        return "No Form"

    view_application_form.short_description = 'Application Form'

admin.site.register(Registration, RegistrationAdmin)

