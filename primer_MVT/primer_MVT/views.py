from django.http import HttpResponse
from datetime import datetime
from django.template import (Template, Context, loader)
from family_app.models import Familia

def familia(
    self, nombre: str = 'nombre', 
    apellido: str = 'apellido', 
    parentesco: str = 'parentesco', 
    edad: int = 'edad'):
    template = loader.get_template('familia.html')
    familia = Familia(nombre=nombre, apellido=apellido, parentesco=parentesco, edad=edad)
    familia.save()
    context_dict = {'nombre' : nombre , 
    'apellido' : apellido, 
    'parentesco' : parentesco, 
    'edad' : edad,
    'ahora': datetime.now(),
    }
    render = template.render(context_dict)
    return HttpResponse(render)