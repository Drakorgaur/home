from django.contrib import admin
from .models import User, Guest, Visitor

admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Visitor)
