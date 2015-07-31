from django.contrib import admin

from .models import (Student, Class, Group, Membership)

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Group)
admin.site.register(Membership)
