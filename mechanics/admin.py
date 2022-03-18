from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User),
admin.site.register(Mechanic)
admin.site.register(Client)
admin.site.register(WorkDone)
admin.site.register(UserProfile)
