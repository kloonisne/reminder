from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import tbl_rmndr
from .forms import ReminderForm
import datetime;
# def index(response, ids):
#     ls = tbl_rmndr.objects.get(id=ids)
#     return HttpResponse("<h1>%s <h1>" % ls.reminder)
def rmlist(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = ReminderForm()
        else:
            reminder = tbl_rmndr.objects.get(pk=id)
            form = ReminderForm(instance=reminder)
        return render(request, "remindme/addrm.html", {'form': form})
    else:
        if id == 0:
            form = ReminderForm(request.POST)
        else:
            reminder = tbl_rmndr.objects.get(pk=id)
            form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
        return redirect('/show/')

def showrmndr(request):
    context ={'reminders':tbl_rmndr.objects.all()}
    return render(request, "remindme/list.html", context)



def rmdelete(request,id):
    reminder = tbl_rmndr.objects.get(pk=id)
    reminder.delete()
    return redirect('/show/')


def todayrm(request):
    v = datetime.datetime.now().date()
    num = tbl_rmndr.objects.filter(rmdate=v).count()
    context = {'reminders': tbl_rmndr.objects.filter(rmdate=v),'num':num}
    return render(request, "remindme/today.html", context)