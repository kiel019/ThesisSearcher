from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Thesis, Comment

def search_thesis(request):
    query = request.GET.get('q')
    if query:
        # Search by title or keywords
        theses = Thesis.objects.filter(Q(title__icontains=query) | Q(keywords__word__icontains=query))
    else:
        theses = Thesis.objects.all()
    return render(request, 'search.html', {'theses': theses})

def add_comment(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)

    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        comment = Comment(thesis=thesis, author=author, content=content)
        comment.save()

    return render(request, 'thesis_detail.html', {'thesis': thesis})