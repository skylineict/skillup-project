from django.urls import path
from .dashboard import Dash, studentchart,userprofile, approved_admission
from .studentstatis import UserStatics,user_courseList,UserDetailsVeiw
from .add_cohorts import AddListUser,studentadd,listcourses,fitterbycourse,users_search,add_user_to_cohort,Cohort_List
from cohorts.views import ListAdminCohort,CreateCohort,CohortList,DeleteCohortList
from .add_project import Add_Projectview
from .projects import Projects




urlpatterns = [
   
    path('',Dash.as_view(), name='dash'),
    path('student', studentchart, name='student'),
    path('pending_admission', userprofile, name='pending'),
    path('approved_admin/<int:id>/', approved_admission, name="admin"),
    path('add_userlist', AddListUser.as_view(), name='addlist'),
    path('addapi', studentadd, name='add'),
    path('listcourse', listcourses, name='courses'),
    path('fitterbycourse', fitterbycourse, name='fitterbycourse'),
    path('usersearch', users_search, name='users_search'),
    path('usersstats', UserStatics.as_view(), name='statis'),
    path('userList/<int:course_id>', UserDetailsVeiw.as_view(), name='userList'),
    path('user_courselist/<int:course_id>', user_courseList, name='user_courselist'),
    path('add_user_cohort', add_user_to_cohort, name='user_cohort'),
    path('list_cohort', Cohort_List, name='list_cohort'),

    #url from cohort app
    path('cohortlist', ListAdminCohort.as_view(), name='admincohort'),
    path('createcohort', CreateCohort.as_view(), name='createcohort'),
    path('cohort_list', CohortList.as_view(), name='cohortlist'),
    path('cohortdelete/<int:cohort_id>', DeleteCohortList, name='deletecohort'),

    #student project url
    path('add_project',Add_Projectview.as_view(), name='add_project' ),
    path('project', Projects.as_view(), name='projects')
 









    
    

]
