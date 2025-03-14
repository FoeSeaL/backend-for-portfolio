from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency percentage (0-100)")
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"