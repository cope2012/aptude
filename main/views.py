from django.shortcuts import render
from django.views.generic import TemplateView
from .forms.main_form import MainForm


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MainForm

        return context
