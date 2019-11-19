from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .models import Ufile
from .forms import UfileForm

class UfileView(View):
    form_class = UfileForm
    template_name = 'ufiles/create_file.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.user=request.user
            file.save()
            link=str(request.get_host())+"/media/"+str(file.fileloc)
            return HttpResponse("YOUR LINK-"+link+("<br/><a href='{}'></a>".format(link)))
        else:
            print('Not Validates', request.POST, form.data['fileloc'])

        return render(request, self.template_name, {'form': form})

def ShowFiles(request):
    template="ufiles/show_files.html"
    files=Ufile.objects.filter(user=request.user)
    return render(request, template, {'files':files})

