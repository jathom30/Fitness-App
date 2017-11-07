from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.WorkoutListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.WorkoutDetailView.as_view(), name='detail'),
    url(r'^create/$', views.WorkoutCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.WorkoutUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.WorkoutDeleteView.as_view(), name='delete'),
    url(r'^exercise/$', views.ExerciseListView.as_view(), name='exercise_list'),
    url(r'^exercise/(?P<pk>\d+)/$', views.ExerciseDetailView.as_view(), name='exercise_detail'),
]