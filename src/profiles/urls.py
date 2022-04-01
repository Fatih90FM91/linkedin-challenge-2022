from django.contrib import admin
from django.urls import path ,include
from .views import HomeView,ArticleDetail ,CreateJobView

urlpatterns = [
    path('', HomeView.as_view() , name='home' ),
    path('profile_detail/<int:pk>/', ArticleDetail.as_view() , name='profile-detail' ),
    path('add_job/', CreateJobView.as_view() , name='add-job' ),
 
]
