from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.usuario import views
from apps.usuario.views import RegistroUsuario
from apps.usuario.views import inicio

urlpatterns = [
    
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registrar'),
    url(r'^registrar_fundacion$', views.RegistroFundacion, name='registrarfund'),
    url(r'^inicio$', login_required(inicio), name='inicio'),
    
    
]