from django.contrib import admin

from . import models


# create inline for admin view
class ExerciseInline(admin.TabularInline):
    model = models.Exercise

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]


# Register your models here.
admin.site.register(models.Workout, WorkoutAdmin)
admin.site.register(models.Exercise)