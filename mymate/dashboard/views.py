from pyexpat import model
from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.views import generic

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')


def notes(request):
    if request.method=='POST':
        form=Notesform(request.POST)  #by this the data will be save in the form
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
            messages.success(request,'Successfully  added Notes by {}'.format(request.user.username))
    else:    
        form=Notesform()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")



class Notesdetailedview(generic.DetailView):   #generic views is a class but the other views are the functions
    model = Notes


def homework(request):
    homeworks=Homework.objects.filter(user=request.user)
    context={'homeworks':homeworks}
    return render(request,'dashboard/homework.html',context)