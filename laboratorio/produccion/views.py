from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, CreateView
from django.forms import inlineformset_factory, formset_factory,modelformset_factory
from django.views import View

from .models import Equipo,Linea
from .forms import EquipoForm,LineaForm,BaseEquipoFormSet

LineaFormSet = inlineformset_factory(Linea, Equipo, fields=('imei','numero_de_serie','tipodeEquipo','estado'))


# Create your views here.
class Dashboard(TemplateView):
    template_name = 'produccion/dashboard.html'
    
    
class EquipoListView(ListView):
    model = Equipo
    template_name = 'produccion/equipo_list.html'
    context_object_name = 'equipos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de equipos'
        return context


class EquipoUpdateView(UpdateView):
    model = Equipo
    fields = ['estado','linea']
    template_name = 'produccion/equipo_edit.html'
    success_url = reverse_lazy('equipo_list')

    def geto_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['linea'] = Linea.objects.filter(estado='Stock')
        return kwargs
    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        form.fields['linea'].queryset = Linea.objects.filter(estado='Stock')
        return form
    
# class EquipoCreateView(CreateView):
#     model = Equipo
#     formset_class = formset_factory(EquipoForm,extra =1)
#     template_name = 'produccion/equipo_form.html'
#     success_url = reverse_lazy('equipo_list')
#     lineas = Linea.objects.filter(estado='Stock')

#     # formset = formset_class(queryset=lineas)

#     def get(self,request):
#         formset = self.formset_class()
#         return render(request,self.template_name, {'formset':formset})

#     def post(self,request):
#         formset = self.formset_class(request.POST)
        
#         if formset.is_valid():
#             equipos = []
#             for form in formset:
#                 equipo = form.save(commit=False)
#                 equipo.usuario = request.user
#                 equipos.append(equipo)
#             Equipo.objects.bulk_create(equipos)
#             # return redirect('equipo:listar')
#         return render(request, self.template_name,{'formset':formset})

class EquipoCreateView(CreateView):
    model = Equipo
    formset_class = formset_factory(EquipoForm, extra=1, formset=BaseEquipoFormSet)
    template_name = 'produccion/equipo_form.html'
    success_url = reverse_lazy('equipo_list')
    fields = ['numero_de_serie', 'imei', 'tipodeEquipo', 'linea']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        EquipoFormSet = modelformset_factory(Equipo, form=EquipoForm, fields=('imei', 'numero_de_serie', 'tipodeEquipo','linea'))
        data['formset'] = EquipoFormSet(queryset=Equipo.objects.none())
        return data
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['linea'].queryset = Linea.objects.filter(estado='Stock')
        return form

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            equipos = []
            for form in formset:
                equipo = form.save(commit=False)
                equipo.usuario = request.user
                linea = form.cleaned_data['linea']
                equipo.linea = linea
                equipos.append(equipo)
            Equipo.objects.bulk_create(equipos)
            # return redirect('equipo:listar')
        else:
            self.formset = formset
        return self.render_to_response(self.get_context_data(formset=self.formset, linea_form=self.linea_form))



        
class LineaListView(ListView):
    model = Linea
    template_name = 'produccion/linea_list.html'
    context_object_name = 'lineas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de lineas'
        return context    
class LineaUpdateView(UpdateView):
    model = Linea
    fields = ['estado','plan']
    template_name = "produccion/linea_edit.html"
    success_url = reverse_lazy('linea_list')

class LineaCreateView(CreateView):
    formset_class = formset_factory(LineaForm,extra=1)
    template_name = 'produccion/linea_form.html'
    print("hola")

    def get(self,request):
        formset = self.formset_class()
        return render(request,self.template_name, {'formset':formset})

    def post(self,request):
        formset = self.formset_class(request.POST)
        
        if formset.is_valid():
            lineas = []
            for form in formset:
                linea = form.save(commit=False)
                linea.usuario = request.user
                lineas.append(linea)
            Equipo.objects.bulk_create(lineas)
            # return redirect('equipo:listar')
        return render(request, self.template_name,{'formset':formset})
   