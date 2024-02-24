from django.urls import path

from .views import NewestJobView, JobsDetailView, CategoriesView

urlpatterns = [
    path('categories', CategoriesView.as_view()),
    path('jobs', NewestJobView.as_view()),
    path('jobs/<int:pk>', JobsDetailView.as_view()),
]
