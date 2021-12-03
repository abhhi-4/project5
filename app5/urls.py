from django.urls import path
from . import views
urlpatterns = [
    path('hai',views.f1, name='hai'),
    path('abhi',views.f2,name='abhi'),
]