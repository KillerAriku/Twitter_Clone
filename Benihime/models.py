from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#create a tweet
class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name="meep",
        on_delete=models.DO_NOTHING
    )
    body = models.Charfield(max_lenght=200)
    created_at = models.DateTimeField(auto_now_add=True)

def__str__(self):
    return(
            f"{self.user}
            f"({self.created_at:%Y - %M - %d - %H})"
            f"{self.body}..."
                )


        

#from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    follow= models.ManyToManyField("self",
    related_name="followed_by",
    symmetrical=False,
    blank=True)

    date_modified = models.DateTimeField(User,auto_now=True)

    def __str__(self):
        return self.User.username

    
#@receiver(post_save, sender=User)
def create_profile(sender, instance, created , **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
    #have a user follow themselves
    user_profile.follows.set([instance.profile.id])    

post_save.connect(create_profile , sender=User)

