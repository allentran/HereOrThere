from django.db import models

class Votes(models.Model):
	IG_username = models.CharField(max_length=200)
	IG_venueid_winner = models.CharField(max_length=20)
	IG_venueid_loser = models.CharField(max_length=20)
	date_voted = models.DateTimeField('Date Voted')



