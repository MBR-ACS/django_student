from django.db import models
import uuid

# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,unique=True, editable=False, null=False)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


