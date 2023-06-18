from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = 'Hello world page!'
    # return HttpResponse(a)

    text = "новый текст!"
    return render(request, './index.html',{
        'a': a,
        'text': text 
    })
