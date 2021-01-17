from django.urls import path
from . import views
app_name = "campus"
urlpatterns = [
    path('', views.index, name='index'),
    path('listeApprenant/', views.index, name="index"),
    path('listeChambre/', views.ChambreListView.as_view(), name='listeChambre'),
    path('addStudent/', views.addStudent, name='addStd'),
    path('editStudent/<int:pk>/', views.editStudent, name='editStd'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('addChambre/', views.ChambreFormView.as_view(), name="addChambre"),
    path('detailChambre/<int:pk>', views.detailChambre, name="detailChambre"),
    path('detailEtudiant/<int:pk>/', views.EtudiantDetailView.as_view(), name="detailEtudiant")
]