from django import forms
from .models import Skill, SkillCategory

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['name']
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency', 'category']
        widgets = {
            'proficiency': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }