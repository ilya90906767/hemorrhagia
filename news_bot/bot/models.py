from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
    

