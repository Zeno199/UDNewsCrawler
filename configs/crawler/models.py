from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    #author = models.CharField(max_length=10)
    content = models.TextField(blank=True)
    img_url = models.URLField(blank=True)
    created_at = models.DateTimeField(blank=True)

    # format='%Y-%m-%d %H:%M', 
    class Meta:
        managed = True
        verbose_name = 'News'