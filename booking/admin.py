from django.contrib import admin
from .models import Master, Service, Review, Appointment
from django.utils.translation import gettext_lazy as _

class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    search_fields = ('name',)
    list_filter = ('experience',)
    list_editable = ('experience',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_filter = ('price',)
    list_editable = ('price',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'master', 'rating', 'date')
    search_fields = ('client_name', 'comment')
    list_filter = ('rating', 'date')
    list_editable = ('rating',)

    actions = ['delete_low_rating']

    def delete_low_rating(self, request, queryset):
        queryset.filter(rating__lt=3).delete()

    delete_low_rating.short_description = _("Удалить отзывы с рейтингом ниже 3")

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'master', 'service', 'date', 'time')
    search_fields = ('client_name', 'master__name', 'service__name')
    list_filter = ('date', 'time', 'master', 'service')

admin.site.register(Master, MasterAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Appointment, AppointmentAdmin)
