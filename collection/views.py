

#from StackO
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render
from collection.models import File
from collection.forms import FileForm
from collection.forms import InfoForm

from django.template.defaultfilters import slugify

from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request) :
	files = File.objects.all()
	return render(request, 'index.html', {
		'files': files,

		})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            newdoc = File(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the file list after POST
            return HttpResponseRedirect(reverse('webcredit.views.list'))
    else:
        form = InfoForm() # A empty, unbound form

    # Load files for the list page
    files = File.objects.all()

    # Render list page with the files and the form
    return render_to_response(
        'list.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
        )