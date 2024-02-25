from rest_framework import status, authentication, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewestJobView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class BrowseJobsView(APIView):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', ' ')
        if query:
            jobs = jobs.filter(title__icontains=query)
        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))
        serializer = JobSerializer(jobs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

# Can use RetrieveAPIView to fetch individual one
# class JobsDetailView(generics.RetrieveAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobDetailSerializer
#     lookup_fields = ['pk']
class JobsDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
