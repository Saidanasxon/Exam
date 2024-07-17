from django.contrib import admin
from .models import *

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

admin.site.register(Video)

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [VideoInline, ReviewInline]

admin.site.register(Lesson, LessonAdmin)

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

admin.site.register(CustomUser, CustomUserAdmin)

