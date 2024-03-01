from django import forms
from .models import CERT, EmergencyPlan, Resource, Community

class CERTForm(forms.ModelForm):
    class Meta:
        model = CERT
        fields = ['role', 'responsibilities']

class EmergencyPlanForm(forms.ModelForm):
    class Meta:
        model = EmergencyPlan
        fields = ['plan_text']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'location', 'description']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']
