from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('pacientes/', views.PacienteListView.as_view(), name='lista_pacientes'),
    path('pacientes/novo/', views.PacienteCreateView.as_view(), name='novo_paciente'),
    path('pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='detalhe_paciente'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='editar_paciente'),
    path('pacientes/<int:pk>/excluir/', views.PacienteDeleteView.as_view(), name='excluir_paciente'),
    path('consultas/', views.ConsultaListView.as_view(), name='lista_consultas'),
    path('consultas/nova/', views.ConsultaCreateView.as_view(), name='nova_consulta'),
    path('consultas/<int:pk>/', views.ConsultaDetailView.as_view(), name='detalhe_consulta'),
    path('consultas/<int:pk>/editar/', views.ConsultaUpdateView.as_view(), name='editar_consulta'),
    path('consultas/<int:pk>/excluir/', views.ConsultaDeleteView.as_view(), name='excluir_consulta'),
]

