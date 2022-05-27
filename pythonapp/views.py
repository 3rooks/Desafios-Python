from django.shortcuts import render

from pythonapp.models import Family, Contact, Topic
from pythonapp.forms import SearchForm, ContactForm, TopicForm

# Create your views here.


def index(request):
    all_family = Family.objects.all()
    return render(request, 'pythonapp/index.html', {"characters": all_family})

def search(request):
    to_search = request.GET['searching']
    get_search = Family.objects.filter(name__icontains = to_search) or Family.objects.filter(surname = to_search)
    return render(request, 'pythonapp/search.html', {"search":get_search})


def contact(request):
    if request.method == 'POST':
        contact_us=Contact(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
        contact_us.save()

        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            data_form=contact_form.cleaned_data
            return render(request, 'pythonapp/messagesend.html', {'data':data_form})
    else:
        contact_form=ContactForm()

    return render(request, 'pythonapp/contact.html', {'form':contact_form})

def topicform(request):
    if request.method=='POST':
        post_topic=Topic(topic=request.POST['topic'],text=request.POST['text'])
        post_topic.save()

        topic_form=TopicForm(request.POST)
        if topic_form.is_valid():
            data_form=topic_form.cleaned_data
            return render(request, 'pythonapp/topicposted.html', {'data': data_form})
    else:
        topic_form=TopicForm()

    return render(request, 'pythonapp/topic.html', {'form':topic_form})

def rendertopic(request):
    all_topics=Topic.objects.all()
    return render(request, 'pythonapp/rendertopics.html',{'topics':all_topics})