from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import glob
import os
import shutil
from fotos.models import Carpeta


def home(request):
    return render_to_response(
        'home.html',
        {'carpetas': Carpeta.objects.filter(tipo='origen').order_by('ruta')}
    )


def manejador_rutas(request):
    ruta = request.GET['ruta'].strip()
    if ruta == '':
        return render_to_response(
            'error_rutas.html',
            {'error_message': "No ingreso la ruta!!!"},
        )

    if ruta[-1] != '/':
        ruta = ruta + '/'

    if Carpeta.objects.filter(ruta=ruta, tipo='origen').count() == 0:
        c = Carpeta(ruta=ruta, tipo='origen')
        c.save()

    lista_fotos = glob.glob(ruta + '*.jpg')

    if lista_fotos == []:
        return render_to_response(
            'error_rutas.html',
            {'error_message': "No hay ninguna foto en la carpeta especificada"}
        )
    request.session['carpeta_acomodar'] = ruta
    return HttpResponseRedirect(reverse('visor'))


def visor(request):
    lista_fotos = glob.glob(request.session['carpeta_acomodar'] + '*.jpg')

    if lista_fotos == []:
        return render_to_response(
            'visor.html',
            {'error_message': 'No hay mas fotos en esta carpeta'}
        )

    nombreFoto = os.path.basename(lista_fotos[0])
    request.session["foto"] = nombreFoto
    context = {
        'foto': nombreFoto,
        'carpeta_actual': request.session['carpeta_acomodar'],
        'carpetas': Carpeta.objects.filter(tipo='destino').order_by('ruta')
    }

    return render_to_response(
        'visor.html',
        context
    )


def imagen(request, imagen):
    image_data = open(request.session['carpeta_acomodar'] + imagen, "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")


def acomodador(request):
    nueva_ruta = request.GET['nueva_ruta'].strip()
    if nueva_ruta == '':
        return HttpResponseRedirect(reverse('visor'))

    if nueva_ruta[-1] != '/':
        nueva_ruta = nueva_ruta + '/'

    if not os.path.isdir(nueva_ruta):
        os.mkdir(nueva_ruta)

    shutil.move(
        request.session['carpeta_acomodar'] + request.session["foto"],
        nueva_ruta
    )

    if Carpeta.objects.filter(ruta=nueva_ruta, tipo='destino').count() == 0:
        c = Carpeta(ruta=nueva_ruta, tipo='destino')
        c.save()

    return HttpResponseRedirect(reverse('visor'))


def eliminar(request, carpeta_id, tipo):
    c = Carpeta.objects.filter(id=carpeta_id)
    c.delete()
    if tipo == 'destino':
        return HttpResponseRedirect(reverse('visor'))
    else:
        return HttpResponseRedirect(reverse('home'))