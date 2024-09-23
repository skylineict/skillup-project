from django.urls import path
from .dashboard import Dash, studentchart
from .ticketfiles import Ticketfile,pdfexportfiles
from .cohorts import CohortList
from projects.views import ProjectDatials,ProjectVeiw
from user .invests import investment_dashboard,invest





urlpatterns = [
   
    path('',Dash.as_view(), name='dash'),
    path('ticket',Ticketfile, name='ticket'),
    path('sky',pdfexportfiles, name='download'),
    path('student', studentchart, name='student'),
     path('cohorts', CohortList.as_view(), name='cohorts'),


     #url for projects views
   
    path('project/<str:project_id>/', ProjectDatials.as_view(),name='student_projects'),
    path('projects', ProjectVeiw.as_view(),name='project'),
    path('invest', investment_dashboard, name='invest'),
    path('add', invest, name='addinvest'),

    

    

    

]
