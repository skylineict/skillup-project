from django.urls import path
from .views import Postcontent




urlpatterns = [
    path('', Postcontent.as_view(),name='post'),
    

]
