from django.views.generic import View, CreateView
from .forms.main_form import MainForm
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


class MainView(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': MainForm})

    def post(self, request, *args, **kwargs):
        file_url = None
        errors = None
        form = MainForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(f'files/{file.name}', file)
            file_url = fs.url(filename)
        else:
            errors = form.errors

        return render(request, self.template_name, {'form': MainForm, 'file_url': file_url, 'errors': errors})


class StoreFile(CreateView):
    template_name = 'main.html'

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': MainForm})

