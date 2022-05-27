from django.contrib import admin

from pythonapp.models import Family, Topic, Contact

# Register your models here.

admin.site.register(Family)
admin.site.register(Topic)
admin.site.register(Contact)