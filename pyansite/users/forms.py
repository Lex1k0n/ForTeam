from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['name', 'email']

    def clean_repeat_password(self):
        temp_data = self.cleaned_data
        if temp_data['password'] != temp_data['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        else:
            return temp_data['password']



