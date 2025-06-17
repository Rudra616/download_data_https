from django.db import models

# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mob = models.TextField()
    addres = models.TextField()

    
    def __str__(self):
        return self.name