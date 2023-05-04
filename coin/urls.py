from django.urls import path
from .views import TopFiveCoinsView

urlpatterns = [
    path('top-five-coins/', TopFiveCoinsView.as_view(), name='top_five_coins'),
]
