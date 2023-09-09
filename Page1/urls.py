#เลขาห้อง Page1

from django.urls import path
from .views import HomePage

urlpatterns = [
    path('', HomePage), # localhost:8000 / www.Jade.com
]
