from django.urls import path
from inicio.views import inicio, pantalones, medias, crear_pantalon, crear_medias, about, crear_camiseta    
from inicio.views import ListadoCamisetas, CamisetaCrearView, ActualizarCamiseta, DetalleCamiseta ,EliminarCamiseta, DetalleMedias,ActualizarMedias

from django.conf.urls.static import static
from django.conf import settings

# from django.contrib.auth.views import LogoutView
 

urlpatterns = [
    path("",inicio, name="inicio"),
    
    # path("editar_perfil/password/", CambiarContraseña.as_view(), name="cambiar_pwd"),
    # path("editar_perfil/perfil/", Perfil.as_view(), name="perfil"),

    # path("logout/", LogoutView.as_view(template_name="inicio/logout.html"), name="logout"),
    # path("registrarse/", registro, name="registrarse"),
    # path("editar_perfil/", editar_perfil, name="editar_perfil"),

    path("about/", about, name="about"),

    
    path("pantalones/", pantalones, name="pantalones"),
    path("medias/", medias, name="medias"),
    
    
    # path("camisetas/", camisetas, name="camisetas"),
    path("camisetas/", ListadoCamisetas.as_view(), name="camisetas"),
    
    # path("camisetas/<int:camiseta_id>/", detalle_camiseta , name="detalle_camiseta"),
    path("camisetas/<int:pk>/", DetalleCamiseta.as_view() , name="detalle_camiseta"),    
    path("medias/<int:pk>/", DetalleMedias.as_view() , name="detalle_medias"),

        
    # path("camisetas/<int:camiseta_id>/actualizar/", actualizar_camiseta , name="actualizar_camiseta"),
    path("camisetas/<int:pk>/actualizar/", ActualizarCamiseta.as_view() , name="actualizar_camiseta"),
    path("medias/<int:pk>/actualizar/", ActualizarMedias.as_view() , name="actualizar_medias"),


    # path("camisetas/<int:camiseta_id>/eliminar/", eliminar_camiseta , name="eliminar_camiseta"),
    path("camisetas/<int:pk>/eliminar/", EliminarCamiseta.as_view() , name="eliminar_camiseta"),
    
    
    # path("camisetas/crear/", crear_camiseta, name="crear_camiseta"),
    path("camisetas/crear/", CamisetaCrearView.as_view(), name="crear_camiseta"),
    path("pantalones/crear/", crear_pantalon, name="crear_pantalon"),
    path("medias/crear/", crear_medias, name="crear_medias"), 

    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)