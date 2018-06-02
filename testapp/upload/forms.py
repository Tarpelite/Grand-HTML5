from django import forms


class registerUser(forms.Form):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    ConfirmPass = forms.CharField(max_length=50, widget=forms.PasswordInput)

class loginUser(forms.Form):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
