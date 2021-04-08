from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='media/default-avatar.jpeg',
    upload_to='users/',
    null=True,
    blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name) 
    
    def get_profile_image(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        else:
            return 'https://www.google.com/search?q=avatar+png&sxsrf=ALeKk00vWBFNb1Yivi7s6uOswOvgugAUyQ:1617896754727&tbm=isch&source=iu&ictx=1&fir=yURmpEUYR7isQM%252C0Inew68qLw2PbM%252C_&vet=1&usg=AI4_-kQoNXMd53crx_dzbSI_XIrCg9HVvQ&sa=X&ved=2ahUKEwjL2uSK_-7vAhUhy4UKHTzTBvcQ9QF6BAgIEAE#imgrc=yURmpEUYR7isQM'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()