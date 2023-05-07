from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shift.views import ShiftViewSet

app_name = 'shift'

router = DefaultRouter()

router.register('', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls))
]
