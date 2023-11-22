from datetime import datetime

from django.urls import path
from cuentas.views import login,registro, editar_perfil, CambiarContraseña, Perfil
from django.contrib.auth.views import LogoutView




urlpatterns = [
    
    path("login/", login, name="login"),
    path("logout/", LogoutView.as_view(template_name="cuentas/logout.html"), name="logout"),
    path("registrarse/", registro, name="registrarse"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("editar_perfil/password/", CambiarContraseña.as_view(), name="cambiar_pwd"),
    path("editar_perfil/perfil/", Perfil.as_view(), name="perfil"),



]