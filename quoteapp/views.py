from django.shortcuts import render, redirect, get_object_or_404
from quoteapp.forms import QuoteForm, AuthorForm
from quoteapp.models import Author, Quote


# Create your views here.
def main(request):
    quotes = Quote.objects.select_related('author').all()

    return render(request, 'base.html', {'quotes': quotes})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
    else:
        form = AuthorForm()
    return render(request, 'authors/add_author.html', {'form': form})


def add_quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_authors = Author.objects.filter(last_name__in=request.POST.getlist('last_name'))
            for author in choice_authors.iterator():
                new_quote.authors.add(author)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quotes/add_quote.html', {'authors': authors, 'form': form})

    return render(request, 'quotes/add_quote.html', {'authors': authors, 'form': QuoteForm()})


def detail_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/detail.html', {'author': author})

