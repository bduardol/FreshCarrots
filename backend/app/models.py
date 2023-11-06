from django.db import models

class user(models.Model):
  firt_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=100)
  cpf = models.CharField(unique=True, max_length=11,  primary_key=True)

class book(models.Model):
  name = models.CharField(max_length=30)
  author = models.CharField(max_length=30)
  
  
