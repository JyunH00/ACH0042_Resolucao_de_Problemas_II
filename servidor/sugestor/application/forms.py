from django import forms

class MyForm(forms.Form):
    # For BooleanFields, required=False means that Django's validation
    # will accept a checked or unchecked value, while required=True
    # will validate that the user MUST check the box.
    something_truthy = forms.BooleanField(required=False)
