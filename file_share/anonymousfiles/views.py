from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .models import Afile
from .forms import AfileForm

class AfileView(View):
    form_class = AfileForm
    template_name = 'afiles/create_file.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file=form.save()
            link=str(request.get_host())+"/media/"+str(file.fileloc)
            return HttpResponse("YOUR LINK-"+link+("<br/><a href='{}'></a>".format(link)))
        else:
            print('Not Validates', request.POST, form.data['fileloc'])

        return render(request, self.template_name, {'form': form})

def ShowFile(request, pk):
    template=str(Afile.objects.get(pk=pk).fileloc)
    
    return redirect(template)
