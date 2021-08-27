from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #/news/
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #/news/story 1,2
    path('add-story/', views.AddStoryView.as_view(),name='newStory') # /news/ add-story
]
