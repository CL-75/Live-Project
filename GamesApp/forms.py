from django.forms import Select, ModelForm
from django.forms.widgets import DateInput
from .models import *
from django import forms


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'birthday': 'DOB',
        }
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
        }


class AddGameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'game_genre': Select(attrs={'choices': GAME_GENRES}),
            'game_user_rating': Select(attrs={'choices': USER_RATING}),
        }


class GameForm(forms.Form):
    games = forms.CharField(max_length=80)
