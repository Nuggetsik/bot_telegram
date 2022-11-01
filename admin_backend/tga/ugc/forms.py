from django import forms

from .models import Profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name',
            'description',
            'get_image',
            'price',
            

        )
        widgets = {
            'name': forms.TextInput,
        }

