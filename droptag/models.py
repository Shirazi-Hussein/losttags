from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class tag(models.Model): 
    user = models.ForeignKey(User, 
                        default = 1, 
                        null = True,  
                        on_delete = models.SET_NULL 
                        ) 
    tag_name = models.CharField(max_length=50)
    id_link = models.CharField(max_length=100, blank=True)
    geo_location = models.CharField(max_length=100, blank=True)
    time_met = models.DateField(blank=True)
        
    def __str__(self):
        return self.tag_name

# =============================================================================
# class Owner(models.Model):
#     user = models.CharField(max_length=50)
#     id_link = models.CharField(max_length=100, blank=True)
#     
#     def __str__(self):
#         return self.user
# 
# class Tag(models.Model):
#     owner = models.OneToOneField(
#         Owner,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         default=''
#     )
#     tag_name = models.CharField(max_length=50)
#     id_link = models.CharField(max_length=100, blank=True)
#     geo_location = models.CharField(max_length=100, blank=True)
#     time_met = models.DateField(blank=True)
#         
#     def __str__(self):
#         return self.tag_name
# =============================================================================
