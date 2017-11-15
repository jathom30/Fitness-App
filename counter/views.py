from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import mixins
from . import models

############# WORKOUT VIEWS #################
class WorkoutListView(CreateView, ListView):
    context_object_name = 'workouts'
    model = models.Workout
    fields = ('title', 'description')
    template_name = 'counter/workout_list.html'



class WorkoutDetailView(DetailView, UpdateView):
    fields = ('title', 'description')
    model = models.Workout
    template_name = 'counter/workout_detail.html'


class WorkoutCreateView(CreateView):
    fields = ('title', 'description')
    model = models.Workout
    template_name = 'counter/workout_create.html'


class WorkoutUpdateView(UpdateView):
    fields = ('title', 'description')
    model = models.Workout

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.name)


class WorkoutDeleteView(DeleteView):
    model = models.Workout
    success_url = reverse_lazy('counter:list')


############ Exercise views ##############
class ExerciseCreateView(CreateView):
    fields = ('title', 'muscule_group', 'equipment', 'sets', 'reps', 'weight', 'workout')
    model = models.Exercise
    template_name = 'counter/exercise_create.html'
    success_url = reverse_lazy('counter:list')


class ExerciseDetailView(DetailView):
    context_object_name = 'exercise'
    # fields = ('title', 'equipment')
    model = models.Exercise
    template_name = 'counter/exercise_detail.html'


class ExerciseUpdateView(UpdateView):
    fields = ('title', 'muscule_group', 'equipment', 'sets', 'reps', 'weight', 'workout')
    model = models.Exercise


class ExerciseDeleteView(DeleteView):
    model = models.Exercise
    success_url = reverse_lazy('counter:list')