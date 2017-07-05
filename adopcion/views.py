# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adopcion.models import Persona, Solicitud
from adopcion.forms import PersonaForm, SolicitudForm




def index_adopcion(request):
	return HttpResponse("pagina principal de la app adopcion")

class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')


class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')


