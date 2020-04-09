from django.db import models

# Create your models here.
class register(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    # securityQuestion = models.ForeignKey('Security', on_delete=models.CASCADE)
    # securityAnswer = models.CharField(max_length=100)

    def __str__(self):
        return self.username
