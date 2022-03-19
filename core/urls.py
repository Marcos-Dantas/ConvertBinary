from django.urls import path
from core.views import NumberView

urlpatterns = [
    path('', NumberView.as_view(), name='index'),
]