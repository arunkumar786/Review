from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.
from .models import Pet
from symbol import except_clause
def home(request):
    # get the list of pets
    pets = Pet.objects.all()
    # here we use render instead of
    # http response
    return render(request, 'home.html', {'pets':pets})
    #return HttpResponse("<p> home view</p>")


def pet_detail(request,id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not Found')
    #return HttpResponse('<p> pet_detail view with id{}</p>'.format(id))
    return render(request, 'pet_detail.html', {'pet':pet})