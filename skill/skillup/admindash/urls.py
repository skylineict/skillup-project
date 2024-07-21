from django.urls import path
from .dashboard import Dash, studentchart,userprofile, approved_admission




urlpatterns = [
   
    path('',Dash.as_view(), name='dash'),
    path('student', studentchart, name='student'),
    path('pending_admission', userprofile, name='pending'),
    path('approved_admin/<int:id>/', approved_admission, name="admin")

    
    

]
