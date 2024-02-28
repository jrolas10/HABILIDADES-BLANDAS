from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from Cuestionario.models import Encuestado, Pregunta, Respuesta, Carrera, Grupo, Categoria
from django.shortcuts import get_object_or_404
from .decorators import encuestado_autenticado


def home(request):
    plantilla = get_template('inicio.html')
    return HttpResponse(plantilla.render())

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def base_graficas(request):
    plantilla = get_template('base_graficas.html')
    return HttpResponse(plantilla.render())


def formulario(request):
    # Obtener carreras y grupos desde la base de datos
    carreras = Carrera.objects.values_list('nombre', flat=True).distinct()
    grupos = Grupo.objects.values_list('nombre', flat=True).distinct()

    context = {
        'carreras': carreras,
        'grupos': grupos,
    }

    plantilla = get_template('formulario.html')
    return HttpResponse(plantilla.render(context, request))


@encuestado_autenticado
def innovacion(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_innovacion = Categoria.objects.get(nombre='innovacion')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_innovacion)
        return render(request, 'PreguntasUno.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

@encuestado_autenticado
def resolucion(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_resolucion = Categoria.objects.get(nombre='resolucion de conflictos')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_resolucion)
        return render(request, 'PreguntasDos.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

@encuestado_autenticado
def liderazgo(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_liderazgo = Categoria.objects.get(nombre='liderazgo')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_liderazgo)
        return render(request, 'PreguntasTres.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def autoconfianza(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_autoconfianza = Categoria.objects.get(nombre='autoconfianza')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_autoconfianza)
        return render(request, 'PreguntasCuatro.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def equilibrio(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_equilibrio = Categoria.objects.get(nombre='equilibrio emocional')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_equilibrio)
        return render(request, 'PreguntasCinco.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def comunicacion(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_comunicacion = Categoria.objects.get(nombre='comunicacion')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_comunicacion)
        return render(request, 'PreguntasSeis.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def trabajo(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_trabajo = Categoria.objects.get(nombre='trabajo en equipo')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_trabajo)
        return render(request, 'PreguntasSiete.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def capacidad(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_capacidad = Categoria.objects.get(nombre='capacidad de escucha')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_capacidad)
        return render(request, 'PreguntasOcho.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)


def flexibilidad(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_flexibilidad = Categoria.objects.get(nombre='flexibilidad')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_flexibilidad)
        return render(request, 'PreguntasNueve.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)


def gestion(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_gestion = Categoria.objects.get(nombre='gestion de tiempo')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_gestion)
        return render(request, 'PreguntasDiez.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)


def autoconocimiento(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_autoconocimiento = Categoria.objects.get(nombre='autoconocimiento')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_autoconocimiento)
        return render(request, 'PreguntasOnce.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)


def autocontrol(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_autocontrol = Categoria.objects.get(nombre='autocontrol')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_autocontrol)
        return render(request, 'PreguntasDoce.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)


def empatia(request):
    encuestado_id = request.session.get('encuestado_id')
    if encuestado_id:
        categoria_empatia = Categoria.objects.get(nombre='empatia')  # Cambia el nombre de la categoría
        preguntas = Pregunta.objects.filter(categoria=categoria_empatia)
        return render(request, 'PreguntasTrece.html', {'preguntas': preguntas, 'encuestado_id': encuestado_id})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)





def terminos_y_condiciones(request):
    plantilla = get_template('terminos_condiciones.html')
    return HttpResponse(plantilla.render())

def exito(request):
    # Obtén el encuestado_id de alguna manera, por ejemplo, desde la sesión
    encuestado_id = request.session.get('encuestado_id')

    # Verifica si se obtuvo un encuestado_id válido
    if encuestado_id:
        encuestado = ObtenerEncuestado(encuestado_id)
        return render(request, 'exito.html', {'encuestado': encuestado})
    else:
        return HttpResponse('Encuestado no encontrado', status=404)

def ObtenerEncuestado(encuestado_id):
    # Suponiendo que tienes un modelo llamado 'Encuestado' con un campo 'id' como clave primaria
    encuestado = get_object_or_404(Encuestado, id=encuestado_id)
    return encuestado




def mi_vista_error_404(request, exception):
    return render(request, '404.html', status=404)



def mostrar_resultados(request, encuestado_id):
    try:
        encuestado = Encuestado.objects.get(id=encuestado_id)
        categorias = Categoria.objects.all()

        # Código para generar gráficos y detalles del encuestado

        return render(request, 'resultados_encuestado.html', {
            'encuestado': encuestado,
            
            # Otros datos necesarios para la plantilla
        })
    
    
    except (Encuestado.DoesNotExist, Categoria.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': str(e)})




def procesarformulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreCompleto')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        estado_civil = request.POST.get('estadoCivil')
        nombre_carrera = request.POST.get('carrera')
        grupo = request.POST.get('grupo')
        semestre = request.POST.get('semestre')
        correo_electronico = request.POST.get('correoElectronico')

        # Obtener la instancia de Carrera correspondiente al nombre proporcionado
        try:
            carrera_obj = Carrera.objects.get(nombre=nombre_carrera)
        except Carrera.DoesNotExist:
            # Manejar el caso cuando la carrera no existe
            return HttpResponse('La carrera seleccionada no existe', status=404)
        try:
            grupo_obj = Grupo.objects.get(nombre=grupo)
        except Grupo.DoesNotExist:
            return HttpResponse('El grupo seleccionado no existe', status=404)
        
        encuestado = Encuestado(
            nombre=nombre,
            edad=edad,
            sexo=sexo,
            estado_civil=estado_civil,
            carrera=carrera_obj,
            semestre=semestre,
            grupo=grupo_obj,
            correo_electronico=correo_electronico
        )
        encuestado.save()
        request.session['encuestado_id'] = encuestado.id  # Guardar el ID en la sesión

        return redirect('innovacion')
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)



def procesar_respuestas(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            # Obtener las preguntas de la categoría 'innovacion'
            categoria_innovacion = Categoria.objects.get(nombre='innovacion')
            preguntas_innovacion = Pregunta.objects.filter(categoria=categoria_innovacion)
            for pregunta in preguntas_innovacion:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('resolucion')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)



def procesar_respuestas_resolucion(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_resolucion = Categoria.objects.get(nombre='resolucion de conflictos')
            preguntas_resolucion = Pregunta.objects.filter(categoria=categoria_resolucion)
            for pregunta in preguntas_resolucion:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('liderazgo')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)



def procesar_respuestas_liderazgo(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_resolucion = Categoria.objects.get(nombre='liderazgo')
            preguntas_resolucion = Pregunta.objects.filter(categoria=categoria_resolucion)
            for pregunta in preguntas_resolucion:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('autoconfianza')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def procesar_respuestas_autoconfianza(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_autoconfianza = Categoria.objects.get(nombre='autoconfianza')
            preguntas_autoconfianza = Pregunta.objects.filter(categoria=categoria_autoconfianza)
            for pregunta in preguntas_autoconfianza:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('equilibrio')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)

def procesar_respuestas_equilibrio(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_equilibrio = Categoria.objects.get(nombre='equilibrio emocional')
            preguntas_equilibrio = Pregunta.objects.filter(categoria=categoria_equilibrio)
            for pregunta in preguntas_equilibrio:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('comunicacion')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)

def procesar_respuestas_comunicacion(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_comunicacion = Categoria.objects.get(nombre='comunicacion')
            preguntas_comunicacion = Pregunta.objects.filter(categoria=categoria_comunicacion)
            for pregunta in preguntas_comunicacion:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('trabajo')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)

def procesar_respuestas_trabajo(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_trabajo = Categoria.objects.get(nombre='trabajo en equipo')
            preguntas_trabajo = Pregunta.objects.filter(categoria=categoria_trabajo)
            for pregunta in preguntas_trabajo:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('capacidad')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def procesar_respuestas_capacidad(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_capacidad = Categoria.objects.get(nombre='capacidad de escucha')
            preguntas_capacidad = Pregunta.objects.filter(categoria=categoria_capacidad)
            for pregunta in preguntas_capacidad:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('flexibilidad')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)



def procesar_respuestas_flexibilidad(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_flexibilidad = Categoria.objects.get(nombre='flexibilidad')
            preguntas_flexibilidad = Pregunta.objects.filter(categoria=categoria_flexibilidad)
            for pregunta in preguntas_flexibilidad:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('gestion')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def procesar_respuestas_gestion(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_gestion = Categoria.objects.get(nombre='gestion de tiempo')
            preguntas_gestion = Pregunta.objects.filter(categoria=categoria_gestion)
            for pregunta in preguntas_gestion:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('autoconocimiento')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def procesar_respuestas_autoconocimiento(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_autoconocimiento = Categoria.objects.get(nombre='autoconocimiento')
            preguntas_autoconocimiento = Pregunta.objects.filter(categoria=categoria_autoconocimiento)
            for pregunta in preguntas_autoconocimiento:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('autocontrol')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)

def procesar_respuestas_autocontrol(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_autocontrol = Categoria.objects.get(nombre='autocontrol')
            preguntas_autocontrol = Pregunta.objects.filter(categoria=categoria_autocontrol)
            for pregunta in preguntas_autocontrol:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('empatia')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def procesar_respuestas_empatia(request):
    if request.method == 'POST':
        encuestado_id = request.session.get('encuestado_id')
        if encuestado_id:
            encuestado = get_object_or_404(Encuestado, pk=encuestado_id)
            
            categoria_empatia = Categoria.objects.get(nombre='empatia')
            preguntas_empatia = Pregunta.objects.filter(categoria=categoria_empatia)
            for pregunta in preguntas_empatia:
                valor_respuesta = request.POST.get(f'pregunta{pregunta.id}', '')
                respuesta = Respuesta(encuestado=encuestado, pregunta=pregunta, valor=valor_respuesta)
                respuesta.save()
            return redirect('exito')
        else:
            return HttpResponse('Encuestado no encontrado', status=404)
    else:
        return HttpResponse('Método no permitido para esta vista', status=405)


def logout_view(request):
    if 'encuestado_id' in request.session:
        del request.session['encuestado_id']
        return redirect('home')
    else:
        return redirect('home')

