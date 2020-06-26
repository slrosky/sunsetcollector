from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   
    path('about/', views.about, name='about'),
    path('sunsets/', views.sunsets_index, name='index'),
    path('sunsets/<int:sunset_id>/', views.sunsets_detail, name='detail'),
    path('sunsets/create/', views.SunsetCreate.as_view(), name='sunsets_create'),
    path('sunsets/<int:pk>/update/', views.SunsetUpdate.as_view(), name='sunsets_update'),
    path('sunsets/<int:pk>/delete/', views.SunsetDelete.as_view(), name='sunsets_delete'),
    path('sunsets/<int:sunset_id>/add_viewing/', views.add_viewing, name='add_viewing'),
    path('sunsets/<int:sunset_id>/assoc_experience/<int:experience_id>/', views.assoc_experience, name='assoc_experience'),
    path('sunsets/<int:sunset_id>/unassoc_experience/<int:experience_id>/', views.unassoc_experience, name='unassoc_experience'),
    path('experiences/', views.ExperienceList.as_view(), name='experiences_index'),
    path('experiences/<int:pk>/', views.ExperienceDetail.as_view(), name='experiences_detail'),
    path('experiences/create/', views.ExperienceCreate.as_view(), name='experiences_create'),
    path('experiences/<int:pk>/update/', views.ExperienceUpdate.as_view(), name='experiences_update'),
    path('experiences/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experiences_delete'),
]