from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

User = settings.AUTH_USER_MODEL

class tag(models.Model): 
    user = models.ForeignKey(User, 
                        default = 1, 
                        null = True,  
                        on_delete = models.SET_NULL 
                        ) 
    tag_name = models.CharField(max_length=50, default='')
    id_link = models.CharField(max_length=100, blank=True)
    geo_location = models.CharField(max_length=100, blank=True)
    time_met = models.DateField(blank=True)
    date_filled = models.DateTimeField(auto_now_add=True, blank=True)
        
    def __str__(self):
        return self.tag_name

