from django.shortcuts import render
from .models import Thesis

def search_thesis(request):
    query = request.GET.get('q')
    if query:
        theses = Thesis.objects.filter(title__icontains=query)
    else:
        theses = Thesis.objects.all()
    return render(request, 'search.html', {'theses': theses})