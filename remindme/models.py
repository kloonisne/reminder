from django.db import models

# Create your models here.
class tbl_rmndr(models.Model):
    reminder=models.TextField()
    rmdate=models.DateField()

    def __str__(self):
        return self.reminder