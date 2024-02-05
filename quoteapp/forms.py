from django.forms import ModelForm

from quoteapp.models import Quote, Author


# Defining the AuthorForm
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', 'birth_place', 'description']

# Defining the QuoteForm
class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['quote_text', 'author']
