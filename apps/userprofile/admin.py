from django.contrib import admin

from .models import Profile
# Register your models here.

admin.site.register(Profile) #this line allows the profile 
                            # model to be visible on the admin 
                            #site
