from django.shortcuts import render
from Cuestionario.models import Encuestado, Categoria, Pregunta, Respuesta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

# Las funciones restantes se mantienen igual

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

def calcular_porcentaje_habilidad(valor):
    return (valor / 5) * 100

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

def generar_grafica_general(encuestado, categorias):
    plt.figure(figsize=(12, 8))
    colores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightblue', 'pink', 'yellow', 'cyan', 'magenta', 'lime', 'lavender', 'gold', 'teal']
    promedios = []
    total_preguntas = 0
    total_puntos = 0

    for i, categoria in enumerate(categorias):
        preguntas_categoria = Pregunta.objects.filter(categoria=categoria)
        valores_categoria = []

        for pregunta in preguntas_categoria:
            respuestas_pregunta = Respuesta.objects.filter(encuestado=encuestado, pregunta=pregunta)
            valor_respondido = respuestas_pregunta[0].valor if respuestas_pregunta.exists() else 0
            valores_categoria.append(valor_respondido)

        promedio_categoria = sum(valores_categoria) / len(valores_categoria) if valores_categoria else 0
        promedios.append(promedio_categoria)

        porcentaje_categoria = calcular_porcentaje_habilidad(promedio_categoria)
        plt.text(i, max(promedios) * 1.05, f"{porcentaje_categoria:.2f}%", ha='center')

        total_preguntas += len(valores_categoria)
        total_puntos += sum(valores_categoria)

    porcentaje_general = calcular_porcentaje_habilidad(total_puntos / total_preguntas) if total_preguntas > 0 else 0
    mensaje_general = generar_mensaje_porcentaje(porcentaje_general)

    plt.text(6, plt.ylim()[1] * 5.5, f"Habilidades blandas: {porcentaje_general:.2f}%, {mensaje_general}", ha='center', fontweight='bold')
    plt.bar([ajustar_texto(categoria.nombre, max_length=20) for categoria in categorias], promedios, color=colores)
    plt.ylabel('Promedio de Respuestas')
    plt.title('Promedio de respuestas por categoría')
    plt.ylim(0, 5)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    grafico_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return grafico_base64

def generar_graficas_por_categoria(encuestado, categorias):
    graficos_base64 = {}
    colores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightblue']

    for categoria in categorias:
        preguntas_categoria = Pregunta.objects.filter(categoria=categoria)

        plt.figure(figsize=(10, 6))
        valores_categoria = []

        for i, pregunta in enumerate(preguntas_categoria):
            respuestas_pregunta = Respuesta.objects.filter(encuestado=encuestado, pregunta=pregunta)
            valor_respondido = respuestas_pregunta[0].valor if respuestas_pregunta.exists() else 0

            texto_etiqueta = ajustar_texto(pregunta.texto)
            plt.bar(texto_etiqueta, valor_respondido, color=colores[i % len(colores)] )

            porcentaje_habilidad = calcular_porcentaje_habilidad(valor_respondido)
            plt.text(i, valor_respondido * 1.05, f"{porcentaje_habilidad:.2f}%", ha='center')

            valores_categoria.append(valor_respondido)

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

def mostrar_graficos_personal(request, encuestado_id):
    try:
        encuestado = Encuestado.objects.get(id=encuestado_id)
        categorias = Categoria.objects.all()
        
        grafico_general_base64 = generar_grafica_general(encuestado, categorias)
        graficos_base64 = generar_graficas_por_categoria(encuestado, categorias)

        detalles_encuestado = {
            'nombre': encuestado.nombre,
            'grupo': encuestado.grupo.nombre,
            'carrera': encuestado.carrera.nombre,
            'semestre': encuestado.semestre,
            'edad': encuestado.edad,
            'correo': encuestado.correo_electronico,
        }

        encuestados = Encuestado.objects.all()
        return render(request, 'resultados_encuestado.html', {
            'encuestado': encuestado,
            'graficos_base64': graficos_base64,
            'detalles_encuestado': detalles_encuestado,
            'encuestados': encuestados,
            'grafico_general': grafico_general_base64,
        })

    except (Encuestado.DoesNotExist, Categoria.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': str(e)})
