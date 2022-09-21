from django.db import models
from home.models import Configuration

class Client(models.Model):
	name = models.CharField(max_length= 40)
	phone = models.CharField(max_length = 15,unique=True)
	email = models.EmailField(unique=True)
	user = models.CharField(max_length = 40)
	password = models.CharField(max_length = 20)
	img = models.ImageField(upload_to = "Logo", default = "photo.jpg")
	block = models.BooleanField(default = False)
	birthday = models.CharField(max_length = 12, null=True, blank= True)

	def __str__(self):
		return self.user


class Wallet_Client(models.Model):
	amount = models.IntegerField()
	client = models.ForeignKey(Client, on_delete=models.CASCADE)

	def __str__(self):
		return self.client.user

	def convert_dollar_to_tokens(self):
		c = Configuration.objects.last()
		return int(float(self.amount) / c.value_token)



