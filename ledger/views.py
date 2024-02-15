from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO PO")

def recipe_list(request):
    ctx = {
        "tasks":[
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4',
        ]
    }

    return render(request, 'recipe_list.html', ctx)