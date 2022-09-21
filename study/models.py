from django.db import models

class Study(models.Model):
	name_study = models.CharField(max_length= 40, unique = True)
	pswd = models.CharField(max_length=20)
	email = models.EmailField(unique = True)
	birthday = models.CharField(max_length = 12)
	block = models.BooleanField(default= False)
	independent = models.BooleanField(default= False)

	def __str__(self):
		return self.name_study


class Information(models.Model):
	key_private = models.CharField(max_length = 150)	
	n_transaction = models.CharField(max_length = 150, default= "AD000000000000001")
	study = models.ForeignKey(Study,on_delete = models.CASCADE)
