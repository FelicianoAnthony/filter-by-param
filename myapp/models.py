from django.db import models
from django.core.exceptions import ValidationError




class Operator(models.Model): 
	first_name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)


	

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name) 


	def capitalize(self, word):
		if word[0].islower():
			raise ValidationError('Please make first letter uppercase - {}'.format(word))

	def validate_unique(self, exclude=None):
		"""
		can also do this within Operator class 
			# class Meta:
			# 	unique_together = ('first_name', 'last_name')
		"""
		operators = Operator.objects.all()
		# import pdb; pdb.set_trace()
		for operator in operators:
			if operator.first_name == self.first_name and operator.last_name == self.last_name: 
				raise ValidationError('Combination of first & last name alreads exists in DB = {} {}'.format(operator.first_name, operator.last_name))

		self.capitalize(self.first_name)
		self.capitalize(self.last_name)


	def save(self, *args, **kwargs): 
		"""
		validate data before saving
		"""
		self.validate_unique()
		return super(Operator, self).save(*args, **kwargs) 






class Site(models.Model):
	location = models.CharField(max_length=5)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(blank=True, null=True)
	deleted = models.DateTimeField(blank=True, null=True)
	operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

	def __str__(self):
		return self.location 



class Computer(models.Model):
	hostname = models.CharField(max_length=10, unique=True)
	bfid = models.CharField(max_length=20, unique=True)
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(blank=True, null=True)
	deleted = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.hostname





