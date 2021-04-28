from django import forms


class FormcContact(forms.Form):
    name=forms.CharField(label="Nombre", required=True)
    last_name=forms.CharField(label="Apellido", required=True)
    email=forms.EmailField(label="Email", required=True)
    contenido=forms.CharField(label="Comentarios", required=True)
    