from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import calculator_view, clear_history, CalculationViewSet

router = DefaultRouter()
router.register('calculations', CalculationViewSet, basename='calculations')

urlpatterns = [
    path('', calculator_view, name='calculator'),
    path('clear-history/', clear_history, name='clear_history'),
    path('api/', include(router.urls)),
]
