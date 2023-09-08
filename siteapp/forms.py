from django import forms
from.models import *
from django.core.exceptions import ValidationError


class CountriesForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=30)
    is_published = forms.BooleanField(required=False, label='Publish this post')

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'addpage':
            raise ValidationError(f'Slug may not be {new_slug}')
        if Countries.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique.We have ({new_slug}) slug already')

        return new_slug


    def save(self):
        new_countries = Countries.objects.create(
            title = self.cleaned_data['title'],
            slug = self.cleaned_data['slug'],
            is_published = self.cleaned_data['is_published'],
        )