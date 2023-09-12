from django import forms

class EmailForm(forms.Form):
    email_type = forms.ChoiceField(
        choices=[("introductory", "Introductory")],
        required=True,
        widget=forms.Select(attrs={'class': 'input'}),
    )
    prospect_name = forms.CharField(
        label="Prospect Name",
        required=True,
        widget=forms.TextInput(attrs={'class': 'textinput'}),
    )
    prospect_website = forms.CharField(
        label="Prospect Website",
        required=True,
        widget=forms.TextInput(attrs={'class': 'textinput'}),
    )
    job_description = forms.CharField(
        label="Job Description",
        required=True,
        widget=forms.Textarea(attrs={'class': 'textarea'}),
    )

