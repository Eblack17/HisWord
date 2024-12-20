from django.urls import path
from .views import HealthCheckView, GuidanceView

urlpatterns = [
    path('', HealthCheckView.as_view(), name='health_check'),
    path('guidance/', GuidanceView.as_view(), name='guidance'),
]
