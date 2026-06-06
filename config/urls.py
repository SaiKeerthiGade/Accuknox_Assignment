from django.urls import path, include

urlpatterns = [
    path('', include('signals_app.urls')),
]