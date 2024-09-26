from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    useremail = models.EmailField(max_length=254, primary_key=True) 
    password = models.CharField(max_length=255, default="password") 
    username = models.CharField(max_length=100,default='username')

    def save(self, *args, **kwargs):
        # Hash the password before saving if it's in plain text
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
