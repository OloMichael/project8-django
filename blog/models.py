from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)   # short text
    body = models.TextField()                  # long text
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return self.title
