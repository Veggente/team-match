from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from groupem.models import Faculty


def index(request):
    return render(request, 'groupem/index.html')

def signup(request):
    return render(request, 'groupem/signup.html')

def create_user(request):
    # TODO: check passwords.
    role = request.POST.getlist('Role')
    print(role)
    username = request.POST.getlist('username')
    print(username)
    if role == 'Faculty':
        user = User.objects.create(username=username)
        faculty = Faculty.objects.create(user=user)
    return HttpResponseRedirect(reverse('groupem:index'))

def calendar(request):
    return render(request, 'groupem/calendar.html')
