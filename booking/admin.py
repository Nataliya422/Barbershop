# booking/admin.py
from django.contrib import admin
from .models import Master, Service, Review
from django.utils.translation import gettext_lazy as _


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    search_fields = ('name',)
    list_filter = ('experience',)
    list_editable = ('experience',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
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

admin.site.register(Master, MasterAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)