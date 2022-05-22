from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table='users'

  def __str__(self):
    return self.username + ' ' + self.email

