from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################

# this first of all shows the already added tasks in database 
#inorder of their date

#request basically is the http method like get
#  post etc falls into request
def index(request):

    item_list = Todo.objects.order_by("-date")

#if the request is post, in our case adding a new task
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        
#if it is anything other than post
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

# Create your views here.
