# testDjango

Development of a basic knowledge test about django.
The txt requirements are included, for the installation of the dependencies to be used in a virtual environment

The following is requested in the test:

Por favor si tienes dudas sobre la pregunta dime, lo que busco es medir tus conocimientos en Django basado en la forma que tenemos de trabajar, serán algunas preguntas de cómo resolver algunas situaciones, podemos discutirlas, no necesariamente es una respuesta inmediata. 
Supongamos que trabajamos en un proyecto de agenda telefónica en línea donde cada usuario se registra y puede guardar sus contactos y verlos. Tienes un modelo: 
class Contact(models.Model): 
name = models.Charfield() 
telephone = models.Charfield() 
email = models.Charfield() 
data = models.Charfield() 
user = models.ForeignKey(User)
y un view: 
class Create(CreateView): 
fields=['name', 'telephone', 'email']

¿Supón que todos los usuarios que usan la vista Create ya están loggeados en el sistema, como modificarías la clase Create para que en la variable user del modelo se guarde automáticamente el usuario que creó el registro?
Revisa el modelo que te envié y cuéntame que parámetros obligatorios faltan y si se te ocurre algún otro detalle que mejorar en la redacción del modelo. 
Ahora queremos guardar en data la concatenación del nombre, teléfono y email, de manera que siempre que se modifique la instancia, se mantenga actualizado el valor en data. ¿Cómo modificarías el modelo para lograr esto?
¿Supongamos que para esto alguien ya hizo html de una barra de navegación (navbar.html) y de un formulario genérico (form.html), además todos los estilos necesarios para el proyecto y la estructura global están en un archivo base.html que tiene bloques navbar (para la barra de navegación) y content (para el contenido), como usarias el sistema de templates de Django para armar la vista del Create? (busco una respuesta de 3 o 4 líneas de codigo usando las herramientas que brinda django) 
Escribe una clase que herede de ModelForm y que verifique que se haya llenado al menos un dato entre email y teléfono, ¿cómo cambiarías el create view para usar este formulario con validación? 
Supongamos que por algún motivo la cantidad de campos del modelo Contacto han aumentado demasiado como para listarlos, si te entrego un diccionario: { 'telefono':'55555', 'email': 'mail@mail.com', . . . } como completarías la función cuyos parámetros son una instancia de contacto (contacto) y el diccionario de datos que quieres actualizar donde la llave corresponde al nombre del campo y el valor al nuevo valor deseado (data) ¿Se te ocurren dos formas distintas? 
def actualizar (contacto, data):

Responding with this development, thanks for sharing the test.
 
