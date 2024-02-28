from django.shortcuts import redirect

def encuestado_autenticado(view_func):
    def wrapper(request, *args, **kwargs):
        encuestado_id = request.session.get('encuestado_id')
        if not encuestado_id:
            return redirect('formulario')
        return view_func(request, *args, **kwargs)
    return wrapper
