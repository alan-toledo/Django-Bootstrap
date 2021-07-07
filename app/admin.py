from django.contrib import admin
from .models import User, Task, Priority, Status

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(Status)
