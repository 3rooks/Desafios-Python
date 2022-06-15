from django.shortcuts import render
from django.shortcuts import redirect

from pythonapp.models import Topic
from pythonapp.forms import UserRegisterForm

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'pythonapp/components/topic_list.html'


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'pythonapp/components/topic_detail.html'


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    # template_name 'Opcional' - Defaul => templates/app
    template_name = 'pythonapp/components/topic_update_form.html'
    success_url = reverse_lazy("pythonapp:topic-list")
    fields = ['title', 'text']


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'pythonapp/components/topic_confirm_delete.html'
    success_url = reverse_lazy('pythonapp:topic-list')


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    template_name = 'pythonapp/components/topic_add_form.html'
    success_url = reverse_lazy('pythonapp:topic-list')
    fields = ['title', 'text']


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pythonapp:topic-list')
        else:
            return render(request, 'pythonapp/components/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'pythonapp/components/login.html', {'form': form})


@login_required
def logout_request(request):
    logout(request)
    return redirect("pythonapp:user-login")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "pythonapp/components/register_confirmed.html", {"message": "Successfully Registered User."})
    else:
        form = UserRegisterForm()
    return render(request, "pythonapp/components/register.html", {"form": form})


def Search(request):
    to_search = request.GET['search']
    get_search = Topic.objects.filter(title__icontains=to_search,)
    return render(request, 'pythonapp/components/search.html', {"search": get_search})
