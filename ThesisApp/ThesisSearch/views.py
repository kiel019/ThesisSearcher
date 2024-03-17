from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Thesis, Comment
from django.core.paginator import Paginator

def search_thesis(request):
    query = request.GET.get('q')
    theses = Thesis.objects.all()

    if query:
        theses = theses.filter(Q(title__icontains=query) | Q(keywords__word__icontains=query))

    paginator = Paginator(theses, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'page_obj': page_obj})

def add_comment(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)

    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        comment = Comment(thesis=thesis, author=author, content=content)
        comment.save()

    return render(request, 'thesis_detail.html', {'thesis': thesis})

def landing_page(request):
    return render(request, 'landing.html')