from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        photos = Photo.objects.all()
        friendly_names = [(p.id, p.get_friendly_name()) for p in photos]

        self.fields['[photo]'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
