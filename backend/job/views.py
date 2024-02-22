from rest_framework import status, authentication, permissions 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job, Category
from .serializers import JobSerializer

class NewestJobView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
