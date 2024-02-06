from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()



class SolutionForm(forms.Form):
    user_email = forms.EmailField()
    code = forms.CharField(widget=forms.Textarea)

