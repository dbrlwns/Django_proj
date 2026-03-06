from django import forms

from users.models import User
from django.contrib.auth.forms import PasswordChangeForm



class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # username
        self.fields['username'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Enter username',
            'autocomplete': 'new-username',
            'autofocus': 'autofocus'
        })

        # password1
        self.fields['password1'].widget.attrs.update({
            'autocomplete': 'new-password',
            'class': 'form-control rounded-pill',
            'placeholder': 'Enter password'
        })

        # password2
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Confirm password'
        })

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password1 != password2:
            self.add_error('password2', 'Passwords must match.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit: user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'profile_img',
            'first_name',
            'last_name',
            'email',
            'phone',
        )



