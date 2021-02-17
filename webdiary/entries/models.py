from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    # tags

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."
