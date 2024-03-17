from django.shortcuts import render
from django.db.models import Q
from .models import Thesis

def search_thesis(request):
    query = request.GET.get('q')
    if query:
        # Search by title or keywords
        theses = Thesis.objects.filter(Q(title__icontains=query) | Q(keywords__word__icontains=query))
    else:
        theses = Thesis.objects.all()
    return render(request, 'search.html', {'theses': theses})