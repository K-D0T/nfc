from django.db import models

class SignUpModel(models.Model):
	id=models.AutoField(primary_key=True)
	tag=models.IntegerField(default=0)
	email=models.CharField(max_length=225)
	password=models.CharField(max_length=225)
	objects=models.Manager()