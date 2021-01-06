from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

User = settings.AUTH_USER_MODEL

PLATFORM_CHOICES = (
        ("PSN", "PlayStation Network ID"),
        ("XB", "Xbox Gamertag"),
        ("DC", "Discord Username"),
        ("STM", "Steam Username"),
        )

class tag(models.Model): 
    user = models.ForeignKey(User, 
                        default = 1, 
                        null = True,  
                        on_delete = models.SET_NULL 
                        )
    
    platform = models.CharField(
        default='STM',
        max_length=32,
        choices=PLATFORM_CHOICES)
    tag_name = models.CharField(max_length=50)
    id_link = models.CharField(max_length=100, blank=True)
    geo_location = models.CharField(max_length=100, blank=True)
    time_met = models.DateField()
    date_filled = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.tag_name

