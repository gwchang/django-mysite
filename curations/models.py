from django.db import models

# Create your models here.

class Collection(models.Model):
  title_text = models.CharField(max_length=200)
  author_text = models.CharField(max_length=200)
  description_text = models.CharField(max_length=2000)
  homepage_url = models.CharField(max_length=300)

  def __str__(self):
    return '%s by %s' % (self.title_text, self.author_text)

class Asset(models.Model):
  file_text = models.CharField(max_length=200) 
  title_text = models.CharField(max_length=200)
  link_url = models.CharField(max_length=300)
  price_decimal = models.DecimalField(max_digits=8, decimal_places=2)
  collection = models.ForeignKey(Collection, default=0)

  def __str__(self):
    return self.title_text

