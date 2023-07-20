from django.db import models

# Create the model 
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=100)