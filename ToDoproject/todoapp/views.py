import re
from django.shortcuts import redirect, render
from todoapp.models import ToDoList 
# Create your views here.
from django.core import serializers
from django.http import JsonResponse
from .forms import DeloForm


def main_page(request):
    return render(request,'main_page.html')

def get_data(request):
    todo_list = ToDoList.objects.all()
    ret =[]
    for el in todo_list:
        ret.append({'id':el.id,
                    'delo':el.delo,
                    })
    return JsonResponse(ret,safe=False)

def add_data(request):
    if request.method == 'POST':
        userform = DeloForm(request.POST)
        if userform.is_valid():
            quiz = userform.cleaned_data["delo"]
            new_delo = ToDoList(delo = quiz)
            new_delo.save()
            return get_data(request)
    elif request.method=='GET':
        return redirect('main_page')

def delete_data(request):
    if request.method=='POST':
        delo = ToDoList.objects.get(id=request.POST.get('id'))
        delo.delete()
        return get_data(request)
    elif request.method=='GET':
        return redirect('main_page')