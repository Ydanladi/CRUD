from django.urls import path
from .views import ListCustomers

urlpatterns = [
    path('', ListCustomers.as_view(), name='customers')
    
]
