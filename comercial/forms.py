from django import forms


class SearchForm(forms.Form):
    item_busqueda = forms.CharField(max_length=256, required=False)
