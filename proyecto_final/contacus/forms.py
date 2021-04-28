from django import forms


class FormcContact(forms.Form):
    name=forms.CharField(label="Nombre", required=True)
    last_name=forms.CharField(label="Apellido", required=True)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea, max_length= 300)
    