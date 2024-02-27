from django.urls import path

from .views import NewestJobView, JobsDetailView, CategoriesView, BrowseJobsView, MyJobView, CreateJobView

urlpatterns = [
    path('categories/', CategoriesView.as_view()),
    path('jobs/', NewestJobView.as_view()),
    path('jobs/all/', BrowseJobsView.as_view()),
    path('jobs/my/', MyJobView.as_view()),
    path('jobs/<int:pk>/', JobsDetailView.as_view()),
    path('jobs/create/', CreateJobView.as_view()),
]
