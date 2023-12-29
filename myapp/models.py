from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Careerlog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    execution_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return self.title
