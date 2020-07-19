from django.db import models

class page(models.Model):
	image = models.FileField(default='default.jpg',upload_to='media_cdn/profile_pics')
	fullname=models.CharField(max_length=200, default=None)
	
	def __str__(self):
		return f'{self.fullname} Profile'

