from django.db import models
from django.urls import reverse
class cateogies(models.Model):
	"""This is the main model used for the homepage"""
	name = models.CharField(max_length=80)
	# thumbnail = models.ImageField(upload_to='photos')
	description = models.TextField(max_length=300)
	upload_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Content(models.Model):
	name = models.CharField(max_length=80)
	link = models.CharField(max_length=300)
	acess = models.ManyToManyField(cateogies)

	def __str__(self):
		return self.name

	def __unicode__(self, ):
		return self.name

class Comment(models.Model):
	content = models.ForeignKey(Content,related_name='comment',on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	body = models.TextField(max_length=600)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s-%s' % (self.content,self.name)

	def get_absolute_url(self):
		return reverse('homedetail',kwargs={"pk":self.pk})