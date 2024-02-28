from django.shortcuts import render
from Cuestionario.models import Encuestado, Categoria, Pregunta, Respuesta, Grupo
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Función para ajustar texto si es demasiado largo
def ajustar_texto(texto, max_length=15):
    words = texto.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line + word) <= max_length:
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)
    return '\n'.join(lines)

# Función para calcular el porcentaje de habilidad
def calcular_porcentaje_habilidad(valor):
    return min((valor / 5) * 100, 100)  # Limita el porcentaje máximo a 100

# Función para generar mensajes según el porcentaje obtenido
def generar_mensaje_porcentaje(porcentaje):
    if porcentaje < 20:
        return "Su nivel es muy bajo. Se recomienda trabajar en mejorar estas habilidades."
    elif porcentaje < 40:
        return "El porcentaje obtenido indica que hay margen de mejora."
    elif porcentaje < 60:
        return "Posee un nivel medio, pero todavía hay espacio para mejorar."
    elif porcentaje < 80:
        return "Tiene un buen nivel de habilidades."
    else:
        return "Excelente desempeño en estas habilidades. ¡Sigue así!"

# Función para generar las gráficas del grupo
def generar_grafica_general_grupo(encuestados_grupo, categorias):
    plt.figure(figsize=(12, 8))
    colores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightblue', 'pink', 'yellow', 'cyan', 'magenta', 'lime', 'lavender', 'gold', 'teal']
    promedios_grupo = []
    total_preguntas = 0
    total_puntos = 0

    for i, categoria in enumerate(categorias):
        preguntas_categoria = Pregunta.objects.filter(categoria=categoria)
        valores_categoria = []

        for pregunta in preguntas_categoria:
            valores_pregunta = []

            for encuestado in encuestados_grupo:
                respuestas_pregunta = Respuesta.objects.filter(encuestado=encuestado, pregunta=pregunta)
                valor_respondido = respuestas_pregunta.first().valor if respuestas_pregunta.exists() else 0
                valores_pregunta.append(valor_respondido)

            promedio_pregunta = sum(valores_pregunta) / len(valores_pregunta) if valores_pregunta else 0
            valores_categoria.append(promedio_pregunta)

        promedio_categoria = sum(valores_categoria) / len(valores_categoria) if valores_categoria else 0
        promedios_grupo.append(promedio_categoria)

        porcentaje_categoria = calcular_porcentaje_habilidad(promedio_categoria)
        plt.text(i, max(promedios_grupo) * 1.05, f"{porcentaje_categoria:.2f}%", ha='center', fontweight='bold')

        total_preguntas += len(valores_categoria)
        total_puntos += sum(valores_categoria)

    porcentaje_general_grupo = calcular_porcentaje_habilidad(total_puntos / total_preguntas) if total_preguntas > 0 else 0
    mensaje_general_grupo = generar_mensaje_porcentaje(porcentaje_general_grupo)

    plt.text(6, plt.ylim()[1] * 5.5, f"Habilidades blandas: {porcentaje_general_grupo:.2f}%, {mensaje_general_grupo}", ha='center', fontweight='bold')
    plt.bar([ajustar_texto(categoria.nombre, max_length=20) for categoria in categorias], promedios_grupo, color=colores)
    plt.ylabel('Promedio de Respuestas')
    plt.title('Promedio de respuestas por categoría para el grupo')
    plt.ylim(0, 5)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    grafico_general_grupo_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return grafico_general_grupo_base64

# Resto del código para generar_graficas_por_categoria_grupo() y mostrar_graficos_grupo()...

# Por favor, continúa con el código restante para generar_graficas_por_categoria_grupo() y mostrar_graficos_grupo().
# Asegúrate de aplicar las mejoras mencionadas anteriormente en la lógica y el manejo de datos.
# Código anterior permanece aquí...

# Resto del código...

def generar_graficas_por_categoria_grupo(encuestados_grupo, categorias):
    graficos_base64 = {}
    colores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightblue', 'pink', 'yellow', 'cyan', 'magenta', 'lime', 'lavender', 'gold', 'teal']

    for categoria in categorias:
        preguntas_categoria = Pregunta.objects.filter(categoria=categoria)

        plt.figure(figsize=(10, 6))
        valores_categoria = []

        for i, pregunta in enumerate(preguntas_categoria):
            valores_pregunta = []

            for encuestado in encuestados_grupo:
                respuestas_pregunta = Respuesta.objects.filter(encuestado=encuestado, pregunta=pregunta)
                valor_respondido = respuestas_pregunta.first().valor if respuestas_pregunta.exists() else 0
                valores_pregunta.append(valor_respondido)

            promedio_pregunta = sum(valores_pregunta) / len(valores_pregunta) if valores_pregunta else 0
            valores_categoria.append(promedio_pregunta)

            porcentaje_habilidad = calcular_porcentaje_habilidad(promedio_pregunta)
            plt.bar(ajustar_texto(pregunta.texto, max_length=20), promedio_pregunta, color=colores[i % len(colores)])
            plt.text(i, promedio_pregunta * 1.05, f"{porcentaje_habilidad:.2f}%", ha='center')

        promedio_categoria = sum(valores_categoria) / len(valores_categoria) if valores_categoria else 0
        porcentaje_categoria = calcular_porcentaje_habilidad(promedio_categoria)
        mensaje_categoria = generar_mensaje_porcentaje(porcentaje_categoria)

        plt.ylabel('Valor Respondido')
        plt.title(ajustar_texto(f'Valor respondido a preguntas de {categoria.nombre}, Promedio: {porcentaje_categoria:.2f}%, {mensaje_categoria}', max_length=40))        
        plt.ylim(0, 5)
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        grafico_base64 = base64.b64encode(buffer.getvalue()).decode()
        buffer.close()
        plt.close()

        graficos_base64[categoria.nombre] = grafico_base64

    return graficos_base64

# Resto del código...


def mostrar_graficos_grupo(request):
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo')
        try:
            grupo = Grupo.objects.get(id=grupo_id)
            encuestados_grupo = Encuestado.objects.filter(grupo=grupo)
            categorias = Categoria.objects.all()
            
            grafico_general_grupo_base64 = generar_grafica_general_grupo(encuestados_grupo, categorias)
            graficos_por_categoria_grupo_base64 = generar_graficas_por_categoria_grupo(encuestados_grupo, categorias)

            detalles_grupo = {
                'nombre': grupo.nombre,
                # Otros detalles del grupo
            }

            return render(request, 'grafico_grupo.html', {
                'encuestados_grupo': encuestados_grupo,
                'graficos_por_categoria_grupo': graficos_por_categoria_grupo_base64,
                'detalles_grupo': detalles_grupo,
                'grafico_general_grupo': grafico_general_grupo_base64,
            })

        except (Grupo.DoesNotExist, Encuestado.DoesNotExist, Categoria.DoesNotExist) as e:
            return render(request, 'error.html', {'error_message': str(e)})
    else:
        grupos = Grupo.objects.all()
        return render(request, 'grafico_grupo.html', {'grupos': grupos})
