from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Workout(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('counter:detail', kwargs={'pk': self.pk})


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    MUSCULE_GROUP_CHOICES = (
        ('ch', 'Chest'),
        ('ar', 'Arms'),
        ('le', 'Legs'),
        ('ba', 'Back'),
        ('co', 'Core'),
    )
    muscule_group = models.CharField(
        max_length=2,
        choices=MUSCULE_GROUP_CHOICES,
    )
    EQUIPMENT_USED = (
        ('db', 'Dumbbell'),
        ('bb', 'Barbell'),
        ('bw', 'Body Weight'),
        ('rb', 'Resistance Bands'),
        ('ma', 'Machine'),
    )
    equipment = models.CharField(
        max_length=2,
        choices=EQUIPMENT_USED,
    )
    description = models.TextField(blank=True, default='')
    workout = models.ForeignKey(Workout, related_name='exercises')
    sets = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    weight = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('counter:exercise_detail', kwargs={'pk': self.pk})
