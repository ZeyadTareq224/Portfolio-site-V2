from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=250)
	status = models.TextField(null=True)
	description = models.TextField(null=True)
	screenshot = models.ImageField(null=True, blank=True)
	demo_link = models.CharField(max_length=250, null=True)
	source_code = models.CharField(max_length=250, null=True)


	def __str__(self):
		return self.title


class Certificate(models.Model):
	#title = models.CharField(max_length=250)
	#description = models.TextField()
	cert_image = models.ImageField()		

	def __str__(self):
		return self.title