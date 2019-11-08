from django.contrib import admin

# Register your models here.
from samaneh.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass