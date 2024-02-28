from django.contrib import admin
from django.urls import path, include
from Views import HomeView  # Modificación en la importación
#from Views.ViewGraficas import mostrar_grafica_admin
from Views.graficos import mostrar_graficos
from Views.HomeView import mostrar_resultados
#from Views.graficos import obtener_datos_encuestado
from django.contrib.auth import views as auth_views
from Views.graficoGrupal import mostrar_graficos_grupo
from Views.graficos_personal import mostrar_graficos_personal


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),

    
    path('formulario/', HomeView.formulario, name='formulario'),
    path('procesarformulario/', HomeView.procesarformulario, name='procesarformulario'),
    path('exito/', HomeView.exito, name='exito'),
    path('terminos-y-condiciones/', HomeView.terminos_y_condiciones, name='terminos_y_condiciones'),

    path('innovacion/', HomeView.innovacion, name='innovacion'),
    path('procesar_respuestas/', HomeView.procesar_respuestas, name='procesar_respuestas'),
    
    path('resolucion-de-conflictos/', HomeView.resolucion, name='resolucion'),    
    path('procesar_respuestas_resolucion/', HomeView.procesar_respuestas_resolucion, name='procesar_respuestas_resolucion'),

    path('liderazgo/', HomeView.liderazgo, name='liderazgo'),
    path('procesar_respuestas_liderazgo/', HomeView.procesar_respuestas_liderazgo, name='procesar_respuestas_liderazgo'),

    path('autoconfianza/', HomeView.autoconfianza, name='autoconfianza'),
    path('procesar_respuestas_autoconfianza/', HomeView.procesar_respuestas_autoconfianza, name='procesar_respuestas_autoconfianza'),

    path('equilibrio/', HomeView.equilibrio, name='equilibrio'),
    path('procesar_respuestas_equilibrio/', HomeView.procesar_respuestas_equilibrio, name='procesar_respuestas_equilibrio'),

    path('comunicacion/', HomeView.comunicacion, name='comunicacion'),
    path('procesar_respuestas_comunicacion/', HomeView.procesar_respuestas_comunicacion, name='procesar_respuestas_comunicacion'),

    path('trabajo/', HomeView.trabajo, name='trabajo'),
    path('procesar_respuestas_trabajo/', HomeView.procesar_respuestas_trabajo, name='procesar_respuestas_trabajo'),

    path('capacidad/', HomeView.capacidad, name='capacidad'),
    path('procesar_respuestas_capacidad/', HomeView.procesar_respuestas_capacidad, name='procesar_respuestas_capacidad'),

    path('flexibilidad/', HomeView.flexibilidad, name='flexibilidad'),
    path('procesar_respuestas_flexibilidad/', HomeView.procesar_respuestas_flexibilidad, name='procesar_respuestas_flexibilidad'),

    path('gestion/', HomeView.gestion, name='gestion'),
    path('procesar_respuestas_gestion/', HomeView.procesar_respuestas_gestion, name='procesar_respuestas_gestion'),

    path('autoconocimiento/', HomeView.autoconocimiento, name='autoconocimiento'),
    path('procesar_respuestas_autoconocimiento/', HomeView.procesar_respuestas_autoconocimiento, name='procesar_respuestas_autoconocimiento'),

    path('autocontrol/', HomeView.autocontrol, name='autocontrol'),
    path('procesar_respuestas_autocontrol/', HomeView.procesar_respuestas_autocontrol, name='procesar_respuestas_autocontrol'),

    path('empatia/', HomeView.empatia, name='empatia'),
    path('procesar_respuestas_empatia/', HomeView.procesar_respuestas_empatia, name='procesar_respuestas_empatia'),


    #path('graficos/', mostrar_graficos, name='mostrar_graficos'),
    
    
    path('base-graficas/', HomeView.base_graficas, name='base_graficas'),
    #path('mostrar-grafica/', HomeView.mostrar_grafica, name='mostrar_grafica'),


    #path('obtener_datos_encuestado/<int:encuestado_id>/', obtener_datos_encuestado, name='obtener_datos_encuestado'),
    

    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_view'),
    path('logout/', HomeView.logout_view, name='logout_view'),


    path('mostrar_graficos/', mostrar_graficos, name='mostrar_graficos'),
    path('mostrar_graficos_grupo/', mostrar_graficos_grupo, name='mostrar_graficos_grupo'),
    #path('mostrar_resultados/<int:encuestado_id>/', mostrar_resultados, name='mostrar_resultados'),
    path('mostrar_graficos_personal/<int:encuestado_id>/', mostrar_graficos_personal, name='mostrar_graficos_personal'),
 
]
handler404 = HomeView.mi_vista_error_404
