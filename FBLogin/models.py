from django.db import models

class FBUser(models.Model):
    FBid = models.CharField(max_length=200,primary_key=True)
    DateJoined = models.DateTimeField(auto_now_add=False,verbose_name='Date Joined')
    Location = models.CharField(max_length=200)
    BirthYr = models.CharField(max_length=200)
    Gender = ( ('M','Male'),('F','Female'))
