from django import forms

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, initial='Enter password')

