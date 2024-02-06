from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from quoteapp.forms import QuoteForm, AuthorForm
from quoteapp.models import Author, Quote
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    quote_list = Quote.objects.select_related('author').all()
    paginator = Paginator(quote_list, 3)
    page_number = request.GET.get('page')
    quotes = paginator.get_page(page_number)

    return render(request, 'base.html', {'quotes': quotes})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
    else:
        form = AuthorForm()
    return render(request, 'authors/add_author.html', {'form': form})


@login_required
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

