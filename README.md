# testDjango

Development of a basic knowledge test about django.
The txt requirements are included, for the installation of the dependencies to be used in a virtual environment

The following is requested in the test:

Por favor si tienes dudas sobre la pregunta dime, lo que busco es medir tus conocimientos en Django basado en la forma que tenemos de trabajar, ser�n algunas preguntas de c�mo resolver algunas situaciones, podemos discutirlas, no necesariamente es una respuesta inmediata. 
Supongamos que trabajamos en un proyecto de agenda telef�nica en l�nea donde cada usuario se registra y puede guardar sus contactos y verlos. Tienes un modelo: 
class Contact(models.Model): 
name = models.Charfield() 
telephone = models.Charfield() 
email = models.Charfield() 
data = models.Charfield() 
user = models.ForeignKey(User)
y un view: 
class Create(CreateView): 
fields=['name', 'telephone', 'email']

�Sup�n que todos los usuarios que usan la vista Create ya est�n loggeados en el sistema, como modificar�as la clase Create para que en la variable user del modelo se guarde autom�ticamente el usuario que cre� el registro?
Revisa el modelo que te envi� y cu�ntame que par�metros obligatorios faltan y si se te ocurre alg�n otro detalle que mejorar en la redacci�n del modelo. 
Ahora queremos guardar en data la concatenaci�n del nombre, tel�fono y email, de manera que siempre que se modifique la instancia, se mantenga actualizado el valor en data. �C�mo modificar�as el modelo para lograr esto?
�Supongamos que para esto alguien ya hizo html de una barra de navegaci�n (navbar.html) y de un formulario gen�rico (form.html), adem�s todos los estilos necesarios para el proyecto y la estructura global est�n en un archivo base.html que tiene bloques navbar (para la barra de navegaci�n) y content (para el contenido), como usarias el sistema de templates de Django para armar la vista del Create? (busco una respuesta de 3 o 4 l�neas de codigo usando las herramientas que brinda django) 
Escribe una clase que herede de ModelForm y que verifique que se haya llenado al menos un dato entre email y tel�fono, �c�mo cambiar�as el create view para usar este formulario con validaci�n? 
Supongamos que por alg�n motivo la cantidad de campos del modelo Contacto han aumentado demasiado como para listarlos, si te entrego un diccionario: { 'telefono':'55555', 'email': 'mail@mail.com', . . . } como completar�as la funci�n cuyos par�metros son una instancia de contacto (contacto) y el diccionario de datos que quieres actualizar donde la llave corresponde al nombre del campo y el valor al nuevo valor deseado (data) �Se te ocurren dos formas distintas? 
def actualizar (contacto, data):

Responding with this development, thanks for sharing the test.
 
