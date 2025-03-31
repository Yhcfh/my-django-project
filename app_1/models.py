from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    born = models.IntegerField(null=True, blank=True)
    died = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    known_for = models.CharField(max_length=255, null=True, blank=True)
    notable_work = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    medium = models.CharField(max_length=255, null=True, blank=True)
    dimensions = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    designed_by = models.CharField(max_length=255, null=True, blank=True)
    developer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name