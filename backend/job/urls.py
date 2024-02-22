from django.urls import path

from .views import NewestJobView

urlpatterns = [
    path('', NewestJobView.as_view())    
]
