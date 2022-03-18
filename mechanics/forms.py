from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import transaction

class ClientSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text='e.g JoeBloggs')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=100, help_text='e.g +254798765432')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone_number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.username = self.cleaned_data.get('username')
        user.save()
        client= Client.objects.create(user=user)
        client.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number']

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'location_address']

class EditMechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['service']

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkDone
        fields = ['image_of_work', 'client_name', 'client_contact']