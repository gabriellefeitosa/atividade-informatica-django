from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Paciente, Consulta
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'cadastro/index.html'

class PacienteListView(ListView):
    model = Paciente
    template_name = 'cadastro/paciente_list.html'
    context_object_name = 'pacientes'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'cadastro/paciente_detail.html'
    context_object_name = 'paciente'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nome', 'idade', 'cpf', 'telefone']
    template_name = 'cadastro/paciente_form.html'
    success_url = reverse_lazy('lista_pacientes')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nome', 'idade', 'cpf', 'telefone']
    template_name = 'cadastro/paciente_form.html'
    success_url = reverse_lazy('lista_pacientes')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'cadastro/paciente_confirm_delete.html'
    success_url = reverse_lazy('lista_pacientes')

class ConsultaListView(ListView):
    model = Consulta
    template_name = 'cadastro/consulta_list.html'
    context_object_name = 'consultas'

class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'cadastro/consulta_detail.html'
    context_object_name = 'consulta'

class ConsultaCreateView(CreateView):
    model = Consulta
    fields = ['paciente', 'data', 'hora', 'descricao', 'medico']
    template_name = 'cadastro/consulta_form.html'
    success_url = reverse_lazy('lista_consultas')

class ConsultaUpdateView(UpdateView):
    model = Consulta
    fields = ['paciente', 'data', 'hora', 'descricao', 'medico']
    template_name = 'cadastro/consulta_form.html'
    success_url = reverse_lazy('lista_consultas')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'cadastro/consulta_confirm_delete.html'
    success_url = reverse_lazy('lista_consultas')
