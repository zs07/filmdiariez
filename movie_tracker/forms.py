from django import forms
from movie_tracker.models import Movie

class MovieForm(forms.ModelForm):
    is_favorite = forms.BooleanField(required=False)

    class Meta:
        model = Movie
        fields = ['movie_name', 'details', 'poster', 'date', 'rating', 'review', 'is_favorite']
