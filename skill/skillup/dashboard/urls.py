from django.urls import path
from .dashboard import Dash, studentchart
from .ticketfiles import Ticketfile,pdfexportfiles




urlpatterns = [
   
    path('',Dash.as_view(), name='dash'),
    path('ticket',Ticketfile, name='ticket'),
    path('sky',pdfexportfiles, name='download'),
    path('student', studentchart, name='student')
    

]
