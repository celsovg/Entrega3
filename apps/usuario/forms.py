from django import forms
from apps.usuario.models import  perfilUsuario

from django.contrib.auth.models import User

class perfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = perfilUsuario
        fields = ('foto_perfil',)
        labels = { 'foto_perfil':'Foto de perfil' }

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels ={
            'username' : 'Nombre de usuario',
            'email' : 'Correo electronico',
            'password' : 'Contraseña'
        }
        help_texts = {
            'username' : '',
        }
        error_mesages = {
            'username' : {
                'max_length': 'Maximo 150 caracteres',
                'requiered': 'requerido'
            }, 
            'password': {
                'requiered': 'requerido'
            }

        }
    
    def __init__( self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'from-control'})
        self.fields['password'].widget.attrs.update({'class': 'from-control'})
        self.fields['email'].widget.attrs.update({'class': 'from-control'})