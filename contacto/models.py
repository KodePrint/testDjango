from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Creacion del modelo contacto
class Contact(models.Model):
    name = models.CharField('name', max_length=100)
    telephone = models.CharField('telephone', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    data = models.CharField('data', max_length=100)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.telephone)

    def clean(self, **kwargs):
        super(Contact, self).clean()
        # Guardamos en data la concatenacion de nombre, telefono y email
        self.data = 'Name: %s, Telephone: %s, Email:%s' % (
            self.name, self.telephone, self.email
        )