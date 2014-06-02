from django.db import models

class IDMappings(models.Model):
	FS_id = models.CharField(max_length,primary_key=True)
	IG_id = models.CharField(max_length)

class FSCategories(models.Model):
	FS_catid = models.CharField(max_length)
	FS_name = models.CharField(max_length,primary_key=True)
