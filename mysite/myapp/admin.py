from django.contrib import admin

# Register your models here.
from .models import Question,Choicd,PhoneBook

admin.site.register(Question)
admin.site.register(Choicd)
admin.site.register(PhoneBook)

