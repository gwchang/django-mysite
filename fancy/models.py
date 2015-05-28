from django.db import models

# Create your models here.

class Collection(models.Model):
  title_text = models.CharField(max_length=200)
  author_text = models.CharField(max_length=200)
  description_text = models.CharField(max_length=2000)
  homepage_url = models.CharField(max_length=300)

class Asset(models.Model):
  title_text = models.CharField(max_length=200)
