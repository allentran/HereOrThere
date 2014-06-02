from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from SiteUsers.forms import UserForm
from django.contrib.auth.models import User
from SiteUsers.models import UserProfile,Friends,Education,Location,School
import facebook
import datetime
# get school info and update school DB if need be
def summarize_educ(educ_info):
	school_id = educ_info['school']['id']
	school_type = educ_info['type']
	school_name = educ_info['school']['name']
	school, created = School.objects.get_or_create(school_id=school_id)
	if created:
		school.school_name = school_name
		school.school_type = school_type
		school.save()
	return school

# enter school and user relationship into DB
def enterSchoolUser(education_data,userprofile):
	for school in education_data:
		school = summarize_educ(school)
		user_school,created = Education.objects.get_or_create(user=userprofile,school=school)

# enter friends relationship
def enterFriends(friendsdata,fbuser):
	for friend in friendsdata['data']:
		#need to get userprofile for friend
		try:
			friendprofile = UserProfile.objects.get(fb_id__exact=friend['id'])
			user_friend,created = Friends.objects.get_or_create(person=fbuser,friend=friendprofile)
		except UserProfile.DoesNotExist:
			pass

def enterLocation(locationdata):
	location, created = Location.objects.get_or_create(location_id=locationdata['id'],location_name = locationdata['name'])
	return location
# create Form page or process POST
def register(request):
	if request.method == 'POST': # If the form has been submitted...

		form = UserForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form_data = form.cleaned_data
			fbuser = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
			if fbuser:
				graph = facebook.GraphAPI(fbuser["access_token"])
				fbprofile = graph.get_object("me")
				fbfriends = graph.get_connections("me", "friends")
				fbuser_exists = UserProfile.objects.filter(fb_id=fbprofile['id']).count() > 0
				if fbuser_exists == False:
					user = User.objects.create_user(form_data['username'], form_data['email'], form_data['password'])
					location = enterLocation(fbprofile['location'])
					userprofile = UserProfile(fb_id = fbprofile['id'], user=user, fb_token=fbuser["access_token"],first_name=fbprofile['first_name'],
						last_name=fbprofile['last_name'],location = location,birthyear = datetime.datetime.strptime(fbprofile['birthday'],'%m/%d/%Y').year)
					userprofile.save()
					enterSchoolUser(fbprofile["education"],userprofile)
					enterFriends(fbfriends,userprofile) 

					# send user to verify instagram
					RedirectURI = 'http://'+request.get_host()+reverse('IGsuccess')
					IGUrl = 'https://api.instagram.com/oauth/authorize/?client_id='+settings.IG_CLIENT_ID+'&redirect_uri='+RedirectURI+'&response_type=code'
					return HttpResponseRedirect(RedirectURI)
				else: #fb user already assigned to a user
					return HttpResponse('FB already assigned')
			else: #fb denied
				HttpResponse('you denied fb')
		else: #form not valid
			user_form = UserForm()
			context = {"FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID,'FBPermissions': settings.FACEBOOK_PERMISSIONS,'user_form': user_form}
			return HttpResponse(form.is_valid())
	else:

		user_form = UserForm()
		context = {"FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID,'FBPermissions': settings.FACEBOOK_PERMISSIONS,'user_form': user_form}
		return render(request,"SiteUsers/register.html",context)
