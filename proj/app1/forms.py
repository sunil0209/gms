# your_app/forms.py
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['profile_id', 'subject', 'current_handler', 'created_at', 'updated_at']
        # Add or remove fields based on your model's structure
