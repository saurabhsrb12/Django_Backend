from django.contrib import admin
from .models import Client, Work, Artist
from django.contrib.auth.models import User
from .signals import create_client
from django.db.models.signals import post_save

admin.site.register(Client)
admin.site.register(Work)
admin.site.register(Artist)

# Register signals
post_save.connect(create_client, sender=User)
