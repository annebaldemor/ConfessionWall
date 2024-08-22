from django.shortcuts import redirect, render

from . models import Confession

from . forms import ConfessionForm
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = ConfessionForm(request.POST)
        if form.is_valid(): # check if there are no missing requirments from the form


            form.save()

            return redirect('home') 
    else:
        form = ConfessionForm()

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all().order_by('-date'), # returns a QuerySet an array like data structure
        'form': form

    }


    return render(request, "confession/attempt.html", context)






def about(request):

    form = ConfessionForm()

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all(),
        'form': form

    }

    return render(request, "confession/about.html", context)



















def confess(request):
    if request.method == 'POST':
        form = ConfessionForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('home')
    else:
        form = ConfessionForm()


    return render(request, "confession/confession.html", {'form': form})
