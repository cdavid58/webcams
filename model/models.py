from django.db import models
from study.models import Study
from home.models import Configuration

class Tags(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Modelo(models.Model):
	documentI = models.IntegerField(unique=True)
	name = models.CharField(max_length = 30)
	address = models.TextField()
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=20, unique = True)
	password = models.CharField(max_length = 20)
	block = models.BooleanField(default = False)
	study = models.ForeignKey(Study,on_delete=models.CASCADE,null=True,blank=True)
	img = models.ImageField(upload_to = "Photo_Profile",default = "photo.jpg")
	tags = models.ManyToManyField(Tags,blank=True)
	online = models.BooleanField(default = False)

	def __str__(self):
		return self.username

class Wallet_Model(models.Model):
	amount = models.IntegerField()
	modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)

	def __str__(self):
		return self.modelo.username

	def convert_tokens_to_dollar(self):
		c = Configuration.objects.last()
		return int(float(self.amount) * c.value_token)

