# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




































# from django import forms
# from .models import User
# from django.core.exceptions import ValidationError


# class RegisterForm(forms.ModelForm):
#     firstName = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50,
#         required=True)
#     lastName = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50,
#         required=True)
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50,
#         required=True)
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         label="Confirm your password",
#         required=True)

#     class Meta:
#         model = User
#         fields = ['firstName', 'lastName', 'username',
#                   'password', 'confirm_password', ]

#     def clean(self):
#         super(RegisterForm, self).clean()
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password and password != confirm_password:
#             self._errors['password'] = self.error_class(
#                 ['Passwords don\'t match'])
#         return self.cleaned_data
