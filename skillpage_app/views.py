from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Skill, SkillCategory
from .forms import SkillForm, SkillCategoryForm
from django.views.generic import TemplateView

# Home view
def home(request):
    return render(request, 'index.html')


# About View
class AboutView(TemplateView):
    template_name = 'about-page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any context data you need for the about page here
        # For example:
        # context['page_title'] = 'About Me'
        return context

# Project View
class ProjectView(TemplateView):
    template_name = 'project-page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any context data you need for the project page here
        # For example:
        # context['projects'] = Project.objects.all()  # If you have a Project model
        return context

# Contact View
class ContactView(TemplateView):
    template_name = 'contact-page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any context data you need for the contact page here
        # For example:
        # context['contact_email'] = 'your@email.com'
        return context


# Skills List View
class SkillsListView(ListView):
    model = SkillCategory
    template_name = 'skills.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context

# Skill Create View
class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_form.html'
    success_url = reverse_lazy('skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Skill'
        return context

# Skill Update View
class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_form.html'
    success_url = reverse_lazy('skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Skill'
        return context

# Skill Delete View
class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'skill_confirm_delete.html'
    success_url = reverse_lazy('skills')

# Category Create View
class CategoryCreateView(CreateView):
    model = SkillCategory
    form_class = SkillCategoryForm
    template_name = 'skill_form.html'
    success_url = reverse_lazy('skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Category'
        return context