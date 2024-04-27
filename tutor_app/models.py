from django.db import models

class Tutor(models.Model):

    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=128)  # This should be long enough to store hashed passwords
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Course(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    # Add other fields as needed

    def __str__(self):
        return self.title
