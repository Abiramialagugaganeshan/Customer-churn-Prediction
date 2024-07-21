

from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),  # Root URL for the app
    path('predict/', views.predict, name='predict'),
]
