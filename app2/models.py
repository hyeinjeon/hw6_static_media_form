from django.db import models

# Create your models here.
class Post2(models.Model):
    post2_title = models.CharField(max_length=200)
    post2_writer = models.CharField(max_length=100)
    post2_date = models.DateTimeField()
    post2_body = models.TextField()
    image = models.ImageField(upload_to = "post2/", blank = True, null = True)

    def __str__(self):
        return self.post2_title
        
    def summary(self):
        return self.post2_body[:100]