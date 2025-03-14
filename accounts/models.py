from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator

from phonenumber_field.modelfields import PhoneNumberField



class MyUser(AbstractUser):

	phone_number = models.CharField(max_length = 250 , null = True , blank = True)

	token_send = models.IntegerField(null = True , blank = True)     

	is_admin = models.BooleanField(default=False)
	




	


	








