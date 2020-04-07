from django.db import models

# Create your models here.
class Books(models.Model):
    title: models.CharField()
    author: models.TextField()
    publisher: models.TextField()
    yearOfPublication: models.DateField()
    isbn: models.IntegerField()
    deweyDecimalSystem: models.IntegerField(max_length=3)
    status: models.BooleanField(default=False)

    def __str__(self):
        return self.title