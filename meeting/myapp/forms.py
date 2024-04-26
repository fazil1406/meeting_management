from django import forms

class register(forms.ModelForm):
    First_name=forms.CharField(max_length=100)
    Last_Name=forms.CharField(max_length=100)
    Username=forms.CharField(max_length=100,unique=True)
    Email=forms.EmailField(max_length=300,unique=True)
    Password=forms.CharField(max_length=100,unique=True)
    Confirmpassword=forms.CharField(max_length=100,unique=True)