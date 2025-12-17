from django.urls import path
from .views import calculator_view, clear_history

urlpatterns = [
    path('', calculator_view, name='calculator'),
    path('clear-history/', clear_history, name='clear_history'),
]

