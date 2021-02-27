from django.db import models


class SignUp(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
