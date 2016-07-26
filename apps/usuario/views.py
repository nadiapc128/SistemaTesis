from django.shortcuts import render

# Create your views here.

from apps.usuario.forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroForm

from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def index(request):
	return render(request, 'registration/index.html')

def inicio(request):
	return render(request, 'usuario/inicio.html')


class RegistroUsuario(CreateView):
	model = User
	template_name = "registration/registro_user.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')  #las comillas simples llaman al name de la url

	

def RegistroFundacion(request):
	return render(request, 'registration/registro_fundacion.html')