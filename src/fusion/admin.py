from django.contrib import admin
from fusion.models import Device, UserProfile, AmqpGateway

admin.site.register(Device) 
admin.site.register(UserProfile)
admin.site.register(AmqpGateway)

