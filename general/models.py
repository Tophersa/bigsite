from django.db import models

class Featured(models.Model):
    pageNumber = models.CharField(max_length=1, null=False, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

