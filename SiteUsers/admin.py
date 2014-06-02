from django.contrib import admin
from SiteUsers.models import UserProfile,Friends,Education,Location,School

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(School)
admin.site.register(Education)