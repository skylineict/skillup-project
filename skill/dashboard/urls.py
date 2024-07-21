from django.urls import path
from .dashboard import Dash




urlpatterns = [
   
    path('',Dash.as_view(), name='dash'),

]
