from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('course_roster',)

class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('friends',)

class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)

class MessageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FriendRequest)
admin.site.register(StudyEvent, EventAdmin)
admin.site.register(Message, MessageAdmin)
