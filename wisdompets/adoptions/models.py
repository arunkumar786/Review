from django.db import models

# Create your models here.

class Pet(models.Model):
    # here first index will go to database
    # second index will go to Form
    SEX_CHOICES = [('M','Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    # here inorder to have relation b/w the models 
    # we choose either of the models
    vaccinations = models.ManyToManyField('Vaccine', blank=True)
    def __str__(self):
    	return "%s %s"%(self.species,
    		    self.name)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
    	return self.name
	 		
