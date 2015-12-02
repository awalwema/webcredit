

#from StackO
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.shortcuts import render
from collection.models import File
from collection.models import Transaction
from collection.forms import FileFieldForm

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
    form = FileFieldForm(request.user) # A empty, unbound form

    # Load files for the list page
    files = File.objects.all()
    # Render list page with the files and the form
    return render_to_response(
        'list.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
        )

def create_file(request):
        #if we're coming from a submitted form, do this
    if request.method == 'POST':
        #grab the data from the submitted form and apply to the form
        form = FileFieldForm(request.user,request.POST, request.FILES)
        if form.is_valid():
            myFile = request.FILES['docfile']
            #set the additional details
            newFile = File()
            newFile.user = request.user.userprofile
            newFile.name = request.POST.get('name')
            newFile.docfile = myFile
            newFile.slug = slugify(request.POST.get('name'))
            newFile.description = request.POST.get('description')
            newFile.price = request.POST.get('price')
            transaction = Transaction()
            transaction.user = request.user.userprofile
            transaction.amount = 50
            transaction.save()




            #save the object
            newFile.save()
            #redirect to our newly created file
            return HttpResponseRedirect(reverse('list'))

    #otherwise just create the form
    else:
        form = FileFieldForm(request.user)


    # Render list page with the files and the form
    return render(request, 'Files/create_file.html', {
        'form':form,
        })



