from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rent = models.IntegerField()
    description = models.TextField()

    contact_number = models.CharField(max_length=15)

    image = models.ImageField(upload_to='rooms/', null=True, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rent = models.IntegerField()
    description = models.TextField()
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
