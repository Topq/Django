from django.db import models

# Create your models here.
class BlogsPost(models.Model):
	"""docstring for BlogsPost"""
	 title = models.CharField(max_length= 150)  
     body = models.TextField()  
     timestamp = models.DateTimeField()  