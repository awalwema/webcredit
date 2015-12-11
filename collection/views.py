

#from StackO
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http import HttpResponse

from django.shortcuts import render
from collection.models import File
from collection.models import UserProfile
from collection.models import Transaction
from collection.forms import FileFieldForm
from collection.forms import ProfileForm

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

def create_user_profile(request):
    if request.method == 'POST':
        
        form = ProfileForm(request.user,request.POST)
        if form.is_valid():
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            newProfile = UserProfile()
            newProfile.user = request.user
            newProfile.first_name = firstname
            newProfile.last_name = lastname
            newProfile.balance = 100

            #save the object
            newProfile.save()
            #redirect to our newly created file
            return HttpResponseRedirect(reverse('home'))

    else:
        form = ProfileForm(request.user)

    

    return render(request, 'Files/create_user_profile.html', {
        'form':form,
        })

def file_download(request, slug_id):
    myfile = File.objects.get(slug=slug_id)
    fsock = open('/home/juicebox/projects/webcredit/media/'+str(myfile.docfile), 'r')
    response = HttpResponse(fsock, content_type='text/plain')
    response['Content-Disposition'] = "attachment; filename=%s" % \
                                    (myfile.name)
    return response

def download_page(request, slug_id):
    myfile = File.objects.get(slug=slug_id)
    return render_to_response('public_download_url.html', {'myfile':myfile}, context_instance=RequestContext(request))



