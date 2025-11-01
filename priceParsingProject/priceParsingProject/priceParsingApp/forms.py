from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import listProduct

# --------------------- Registration start --------------------------

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm password"
    )
    

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords are not the same!')
        return cleaned_data
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
# ----------------------- Registration end ----------------------

# ------------------- Product to parse start --------------------

class parseProduct(forms.ModelForm):
    
    class Meta:
        model = listProduct
        fields = '__all__'
        labels = {
            'product_link':'Product link',
            'name':'Name',
        }
        
        #labels = {
        #    'product_link':'Product link',
        #    'name':'Name'
        #}*/
    
    
    