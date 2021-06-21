from django import forms

class FormularioContacto(forms.Form):
    name = forms.CharField(required=True, label="Nombre")
    from_Email = forms.EmailField(required=True,label="Correo")
    subject = forms.CharField(required=True,label="Asunto")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":20}),required=True,label="Mensaje")