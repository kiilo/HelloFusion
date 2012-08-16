from django.contrib.auth.models import User
from django.db import models
 
class UserProfile(models.Model):
    url = models.URLField()
    home_address = models.TextField()
    phone_numer = models.CharField(max_length=20)
    avatar_image = models.ImageField(upload_to='user_images/')
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return str(self.user)

# Create your models here.
class Device(models.Model):
    userProfile = models.ForeignKey(UserProfile, unique=True)
    deviceName = models.CharField(max_length=128)
    homeId = models.CharField(max_length=32)
    authentifcated = models.BooleanField()
    authentificationToken = models.CharField(max_length=24)
    authentificationSecret = models.CharField(max_length=24)
    amqpVhost = models.CharField(max_length=24)
    amqpUser = models.CharField(max_length=24)
    amqpPassword = models.CharField(max_length=24)
    
    def __unicode__(self):
        return str(self.deviceName) 
    
class AmqpGateway(models.Model):
    device = models.ForeignKey(Device, unique=True) 
    amqpVhost = models.CharField(max_length=24)
    amqpUser = models.CharField(max_length=24)
    amqpPassword = models.CharField(max_length=24)
    
    def __unicode__(self):
        return str(self.device) + " " + str(self.amqpVhost)
