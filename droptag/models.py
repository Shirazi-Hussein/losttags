from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.


PLATFORM_CHOICES = (
        ("PSN", "PlayStation"),
        ("XB", "Xbox"),
        ("DC", "Discord"),
        ("STM", "Steam"),
        )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True) 
    name = models.CharField(max_length=200, blank=True) 
    id_link = models.CharField(max_length=200, blank=True) 
    about = models.TextField(blank=True)

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.userprofile.save()

class tag(models.Model): 
    user = models.ForeignKey(User, 
                        default = 1,   
                        on_delete = models.CASCADE 
                        )
    
    platform = models.CharField(
        default='STM',
        max_length=32,
        choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=50)
    id_link = models.CharField(max_length=200, blank=True)
    time_met = models.DateField()
    note = models.TextField(blank=True)
    date_filled = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('tag_display', args=[str(self.id)])
    
            
