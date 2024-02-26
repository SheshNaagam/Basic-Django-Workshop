from django.db import models

# Create your models here.
class Articles(models.Model):
    Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Title = models.CharField(max_length=300)
    Text = models.TextField()

    def __str__(self):
        return self.Title
