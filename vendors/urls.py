from django.urls import path
from .views import *

urlpatterns = [
    path('', VendorList.as_view()),
]