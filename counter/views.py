from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import mixins
from . import models

# Create your views here.
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

    # def get_queryset(self):
    #     if not self.request.user.is_superuser:
    #         return self.model.objects.filter(coach=self.request.user)
    #     return self.model.objects.all()


class ExerciseListView(CreateView, ListView):
    context_object_name = 'exercises'
    model = models.Exercise
    fields = ('title', 'muscule_group', 'equipment', 'sets', 'reps', 'weight', 'workout')
    template_name = 'counter/exercise_list.html'


class ExerciseDetailView(DetailView):
    fields = ('title', 'equipment')
    model = models.Exercise
    template_name = 'counter/exercise_detail'


class ExerciseUpdateView(UpdateView):
    fields = ('title', 'muscule_group', 'equipment', 'sets', 'reps', 'weight', 'workout')
    model = models.Workout

    # def get_page_title(self):
    #     obj = self.get_object()
    #     return "Update {}".format(obj.name)
