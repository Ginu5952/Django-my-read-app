from django import forms 
from apps.core.constants import BOOK_CATEGORY,BOOK_LANGUAGES
from apps.book.models import Tag,Author,Book


class PostBookForm(forms.Form):
    isbn = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"isbn-input",
                "placeholder":"Enter isbn"
            }
        )
        
    )
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"title-input",
                "placeholder":"Enter text"
            }
        )
        
    )
    pages = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                "class":"pages-input",
                "placeholder":"Enter pages"
            }
        )
        
    )

    description = forms.CharField(
        required=False,
        widget = forms.Textarea(
            attrs={
                "class":"description-input",
                "placeholder":"Enter description"
            }
        )
        
    )

    category = forms.ChoiceField(
        widget = forms.RadioSelect(
            attrs={
                "class":"form-cat"
        
            }
        ),
        choices=BOOK_CATEGORY
        
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "tags-select"
            }
        )
    )

    published_year = forms.IntegerField(
        
        widget=forms.NumberInput(
            attrs={
                "class": "published-year-input",
                "placeholder": "Enter published year"
            }
        )
    )

    publisher = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "publisher-input",
                "placeholder": "Enter publisher"
            }
        )
    )

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "authors-input"
            }
        )
    )

    language = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "language-select"
            },
            
        ),choices=BOOK_LANGUAGES,
        initial='en'
    )

    edition = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "edition-input",
                "placeholder": "Enter book editiion"
            }
        )
    )

    book_format = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "book_format-select"
            },
            
        ),choices=[('eb', 'ebook'), ('hc', 'hardcover')]
    )
    
   