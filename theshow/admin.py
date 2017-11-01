from django import forms
from django.contrib import admin

from .models import PageContent
from geography.models import Division


class PageContentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageContentForm, self).__init__(*args, **kwargs)

        self.fields['division'].queryset = Division.objects.filter(
            level__slug='state'
        )


class PageContentAdmin(admin.ModelAdmin):
    form = PageContentForm

admin.site.register(PageContent, PageContentAdmin)
