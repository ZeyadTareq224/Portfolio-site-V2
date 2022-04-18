from django.db import models

# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	content = models.TextField(null=True)
	img = models.ImageField()
	date_created = models.DateTimeField(auto_now_add=True)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title
