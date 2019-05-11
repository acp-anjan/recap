from django.urls import path
from recapapp import views

urlspatterns =[
    path(r'',views.index, name = "recap"),
]