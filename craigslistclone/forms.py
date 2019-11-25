from django import forms
from .models import Listing
from django.core.exceptions import ValidationError


class ListingForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=300)
    image = forms.ImageField(required=True)
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step':0.01}),
        max_digits=6, 
        decimal_places=2,
        min_value=0.01,
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

    pickup_location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True
    )
    
    # place = forms.CharField(
    #     label='Meeting Location',
    #     widget=forms.Select(attrs={'class': 'form-control'},
    #         choices = (
    #             ('0', 'Rotunda'),
    #             ('1', 'Rice Hall'),
    #             ('2', 'O-Hill'),
    #             ('3', '1515 on the Corner'),
    #             ('4', 'McLeod Hall'),
    #         )),
    #     required=True,
    # )
    
    class Meta:
        model = Listing
        fields = ['title', 'price', 'description', 'image', 'condition', 'category', 'pickup_location']
