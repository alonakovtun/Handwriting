from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile

from HandwritingWeb.models import PhotoOfNumber


class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoOfNumber
        fields = ['photo']

        labels = {
            'photo': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update(
            {'class': 'inputfile',
             'onmouseover':'handleFiles(this.files)',
             'onclick':'getId()'})


