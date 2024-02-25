from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

class Category(models.Model):
    title = models.CharField(max_length=255)
    list_display = ["title"]
    
    class Meta:
        ordering = ('-id',)
        verbose_name_plural = "categories"

class Job(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True )
    position_salary = models.CharField(max_length=255)
    position_location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_email = models.EmailField()
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
 
    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')
