from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join


def home(request):
    # form = EmailForm(request.POST or None)
    form = JoinForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        # new_join, created = Join.objects.get_or_create(email=email)
        new_join = form.save(commit=False)
        new_join.save()
    context = {'form': form}
    template = "home.html"
    return render(request, template, context)


def share(request):
    context = {'form': form}
    template = "home.html"
    return render(request, template, context)
