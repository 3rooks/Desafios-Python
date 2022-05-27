from django import forms


class SearchForm(forms.Form):
    search=forms.CharField(max_length=20)

class ContactForm(forms.Form):
    name=forms.CharField(min_length=2, max_length=15)
    email=forms.EmailField()
    subject=forms.CharField(min_length=2, max_length=20)
    message=forms.CharField(max_length=500, widget=forms.Textarea(attrs={'cols':'60','rows':'10'}))

class TopicForm(forms.Form):
    topic=forms.CharField(min_length=2, max_length=20)
    text=forms.CharField(max_length=500, widget=forms.Textarea(attrs={'cols':'60','rows':'10'}))