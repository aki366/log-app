from django.db import models

# CareerlogのDBモデル
class Careerlog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    execution_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
