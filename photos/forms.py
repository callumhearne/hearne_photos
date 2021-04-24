from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('Location', 'desc', 'price',
                  'has_sizes', 'img',
                  'NE',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'Location': 'Location',
            'desc': 'Description',
            'price': 'Price',
            'has_sizes': 'Size',
            'img': 'Photo',
            'NE': 'NE',
        }
