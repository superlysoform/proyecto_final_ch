from django.urls import path
# from inicio.views import inicio, camisetas, pantalones, medias, crear_camiseta, crear_pantalon, crear_medias, actualizar_camiseta, detalle_camiseta, ListadoCamisetas, CamisetaCrearView, ActualizarCamiseta, DetalleCamiseta ,EliminarCamiseta, login, registro
from inicio.views import inicio, pantalones, medias, crear_pantalon, crear_medias
from inicio.views import ListadoCamisetas, CamisetaCrearView, ActualizarCamiseta, DetalleCamiseta ,EliminarCamiseta, login, registro, editar_perfil,CambiarContraseña

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LogoutView
 

urlpatterns = [
    path("",inicio, name="inicio"),
    
    path("login/", login, name="login"),
    path("registrarse/", registro, name="registrarse"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("editar_perfil/password/", CambiarContraseña.as_view(), name="cambiar_pwd"),

    

    path("logout/", LogoutView.as_view(template_name="inicio/logout.html"), name="logout"),

    
    path("pantalones/", pantalones, name="pantalones"),
    path("medias/", medias, name="medias"),
    
    # path("camisetas/", camisetas, name="camisetas"),
    path("camisetas/", ListadoCamisetas.as_view(), name="camisetas"),
    
    # path("camisetas/crear/", crear_camiseta, name="crear_camiseta"),
    path("camisetas/crear/", CamisetaCrearView.as_view(), name="crear_camiseta"),
    
    # path("camisetas/<int:camiseta_id>/", detalle_camiseta , name="detalle_camiseta"),
    path("camisetas/<int:pk>/", DetalleCamiseta.as_view() , name="detalle_camiseta"),
        
    # path("camisetas/<int:camiseta_id>/actualizar/", actualizar_camiseta , name="actualizar_camiseta"),
    path("camisetas/<int:pk>/actualizar/", ActualizarCamiseta.as_view() , name="actualizar_camiseta"),

    # path("camisetas/<int:camiseta_id>/eliminar/", eliminar_camiseta , name="eliminar_camiseta"),
    path("camisetas/<int:pk>/eliminar/", EliminarCamiseta.as_view() , name="eliminar_camiseta"),
    
    path("pantalones/crear/", crear_pantalon, name="crear_pantalon"),
    path("medias/crear/", crear_medias, name="crear_medias"), 

    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)