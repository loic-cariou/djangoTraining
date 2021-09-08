from django import forms

class RecipeForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)
    summury = forms.CharField(required=True, max_length=200)
    content = forms.CharField(required=True)

    