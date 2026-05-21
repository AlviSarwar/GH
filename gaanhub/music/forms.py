from django import forms
from .models import Song, Artist, Album, Playlist


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'genres', 'audio_file', 'cover_image', 'is_premium', 'price']
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(attrs={'placeholder': 'Song title'}),
            'price': forms.NumberInput(attrs={'placeholder': '0.00', 'min': '0', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        artist = kwargs.pop('artist', None)
        super().__init__(*args, **kwargs)
        if artist:
            self.fields['album'].queryset = Album.objects.filter(artist=artist)
        self.fields['album'].required = False
        self.fields['cover_image'].required = False


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your artist name'}),
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
        }


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Playlist name...'}),
        }
