"""from django.urls import path
from .views import test_signal

urlpatterns = [
    path('', test_signal),
]"""

from django.urls import path
from .views import test_signal, transaction_test

urlpatterns = [
    path('', test_signal),
    path('transaction/', transaction_test),
]