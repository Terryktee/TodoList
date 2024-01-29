from django.shortcuts import render,HttpResponseRedirect
from .models import List
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def index(Request):
    list_items = List.objects.order_by('-pub_date')
    template = 'TodoList/index.html'
    current_date = timezone.now()
    if Request.method == "POST":
        new_item = List(
            list_context = Request.POST['list_context'],
        )
        new_item.save()
    context = {
        'list_items':list_items,
        #'checked':checked,
    }

    return render(Request,template,context)

def completed(Request,list_id):
    completed = "text-decoration-line-through"
    list_item = List.objects.get(pk=list_id)
    if Request.method =="POST":
        if Request.POST.getlist['item_status']:
            list_item.complete = True
            list_item.save()
            context = {
                'completed':completed,
            }
            return render(Request,template,context)


def delete(Request,list_id):
    list_item=List.objects.all(pk=list_id)
    template = 'TodoList/index.html'
    list_item.delete()
    context = {
        'list_items':list_item,
    }
    return render(Request,template,context)
