from django.contrib import admin
from django.contrib import admin
from .models import Calculation


# Register your models here.
@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ('user', 'number1', 'operation', 'number2', 'result', 'created_at')
    list_filter = ('operation', 'user')
    search_fields = ('user__username', 'error')
    ordering = ('-created_at',)
