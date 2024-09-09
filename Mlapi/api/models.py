from django.db import models

# Create your models here.
class ImageModel(models.Model):
    name=models.CharField(max_length=200,default='hello')
    image=models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        og_name=self.image.name
        new_name=f"image.jpg"
        self.image.name=new_name
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
    