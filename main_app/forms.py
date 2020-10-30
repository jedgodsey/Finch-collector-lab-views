#### NO IDEA HOW THIS PAGE WORKS
from django import forms
from .models import Client, Claim

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'social', 'final_determination', 'payment_issued', 'payment_received', 'total_award']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_type', 'valid', 'value']
