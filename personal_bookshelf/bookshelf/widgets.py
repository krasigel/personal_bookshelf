from django.forms.widgets import ClearableFileInput


class NoLinkClearableFileInput(ClearableFileInput):
    template_with_initial = '%(input)s'
    template_with_clear = ''

