from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sunset, Experience
from .forms import ViewingForm
# Create your views here.

class SunsetCreate(CreateView):
  model = Sunset
  fields = ['title', 'location', 'description']
  success_url = '/sunsets/'

class SunsetUpdate(UpdateView):
  model = Sunset
  fields = ['description', 'location']

class SunsetDelete(DeleteView):
  model = Sunset
  success_url = '/sunsets/'

def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def sunsets_index(request):
  sunsets = Sunset.objects.all()
  return render(request, 'sunsets/index.html', { 'sunsets': sunsets })

def sunsets_detail(request, sunset_id):
  sunset = Sunset.objects.get(id=sunset_id)
  experiences_sunset_doesnt_have = Experience.objects.exclude(id__in = sunset.experiences.all().values_list('id'))
  viewing_form =  ViewingForm()
  return render(request, 'sunsets/detail.html', { 
    'sunset': sunset, 
    'viewing_form': viewing_form, 
    'experiences': experiences_sunset_doesnt_have
  })

def add_viewing(request, sunset_id):
  form = ViewingForm(request.POST)
  if form.is_valid():
    new_viewing = form.save(commit=False)
    new_viewing.sunset_id = sunset_id
    new_viewing.save()
  return redirect('detail', sunset_id=sunset_id)

def assoc_experience(request, sunset_id, experience_id):
  Sunset.objects.get(id=sunset_id).experiences.add(experience_id)
  return redirect('detail', sunset_id=sunset_id)

def unassoc_experience(request, sunset_id, experience_id):
  Sunset.objects.get(id=sunset_id).experiences.remove(experience_id)
  return redirect('detail', sunset_id=sunset_id)

class ExperienceList(ListView):
  model = Experience

class ExperienceDetail(DetailView):
  model = Experience

class ExperienceCreate(CreateView):
  model = Experience
  fields = '__all__'

class ExperienceUpdate(UpdateView):
  model = Experience
  fields = ['method', 'equipment']

class ExperienceDelete(DeleteView):
  model = Experience
  success_url = '/experiences/'
