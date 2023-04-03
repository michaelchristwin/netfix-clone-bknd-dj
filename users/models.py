from django.db import models


class SignupUser(models.Model):
    email = models.CharField(max_length=55)
    passwordHash = models.CharField(max_length=25)

    def __str__(self):
        return self.email
