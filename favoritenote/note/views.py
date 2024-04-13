from django.shortcuts import render
from django.http import HttpResponse




def index_note(request):
    return render(request, 'note/index_note.html')
