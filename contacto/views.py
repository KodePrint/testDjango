import json

from contacto.form import FormContatc
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.contrib import messages

# Create your views here.

# Creacion de la vista de creacion

class List(ListView):
    model = Contact

class Update(UpdateView):
    model = Contact
    # Al ser correcta la accion nos redirigia a la lista de contactos
    success_url = reverse_lazy('listContact')
    # Ya que utilizaremos un formulario para pasar el User llamamosal atributo
    form_class = FormContatc

class Create(CreateView):
    # Faltaba agregar el a que modelo apunta la vista de creacion
    model = Contact
    # fields = ['name', 'telephone', 'email']
    template_name = 'contacto/contact_form.html'
    # Al ser correcta la accion nos redirigia a la lista de contactos
    success_url = reverse_lazy('listContact')
    # Ya que utilizaremos un formulario para pasar el User llamamosal atributo
    form_class = FormContatc

    # Opcion 1
    ''' Validamos el formulario y agregamos automáticamente al usuario
        esto tomando en cuenta que es necesario estar logeado para llegar a la vista    '''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Opcion 2
    '''En esta opcion no importa que el usuario no este autenticado, ya que le indicamos
    que acepte null y blank en el modelox|'''
    # def post(self, request, *args, **kwargs):
    #     newContact = Contact()
    #     newContact.name = request.POST['name']
    #     newContact.telephone = request.POST['telephone']
    #     newContact.email = request.POST['email']
    #     newContact.user = request.user
    #     newContact.save()
    #     return HttpResponseRedirect(reverse_lazy('ListContact'))

class Delete(DeleteView):
    model = Contact
    success_url = reverse_lazy('listContact')

def actualizar(request, contacto=None, data=None):
    template_name = 'contacto/actualizar_dict.html'
    fields = '__all__'
    success_url = reverse_lazy('listContact')

    if request.method=='GET':
        context = {}

    if request.method=='POST':
        # Validamos si el contacto existe
        if Contact.objects.filter(name=request.POST['contacto']):
            contacto = Contact.objects.filter(name=request.POST['contacto']).get()
            # Obntenemos ladata
            data = request.POST['data']
            # La parseamos a un formato aceptable por json
            new_data = data.replace("'", '"')
            # La convertimos en json
            JSON_data = json.loads(new_data)
            ''' Opcion 1 ORM Django Update '''
            # La actualizamos
            # contacto.update(**JSON_data)

            return redirect(reverse_lazy('listContact'))
        else:
            messages.add_message(request, messages.INFO, 'EL contacto no existe..!')
        context = {}

    return render(request, template_name, context)

    # Dataos de Prueba
    # data = {'telephone': '47243711', 'email': 'prueba@gmail.com', 'data': 'Name: Prueba, Telephone: 47243711, Email: prueba@gmail.com', 'user': '3'}
