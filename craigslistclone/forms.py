from django import forms
from .models import User, Listing
from django.core.exceptions import ValidationError


class ListingForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=3000)
    image = forms.ImageField(required=True)
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step':0.25}),
        max_digits=6, 
        decimal_places=2,
        required=True,
    )
    condition = forms.CharField(
        label='Condition',
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices = (
                ('0', 'Bad'),
                ('1', 'Poor'),
                ('2', 'Decent'),
                ('3', 'Good'),
                ('4', 'New'),
            )),
        required=True,
    )
    category = forms.CharField(
        label='Category',
        widget=forms.Select(attrs={'class': 'form-control'},
            choices = (
                ('TB', 'Textbook'),
                ('FN', 'Furniture'),
                ('CL', 'Clothes'),
                ('EL', 'Electronics'),
                ('OT', 'Other'),
            )),
        required=True,
    )
    class Meta:
        model = Listing
        fields = ['name', 'price', 'description', 'image', 'condition', 'category']


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
