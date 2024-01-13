from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ad_assets/')
    redirect_url = models.URLField()
    impressions = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}"
    
