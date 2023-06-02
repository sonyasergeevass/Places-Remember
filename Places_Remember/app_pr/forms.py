from django import forms


class MemoryForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
    title = forms.CharField(max_length=100, required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Name of the memory'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Description of the memory'}))
