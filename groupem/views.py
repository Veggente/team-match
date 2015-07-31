from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from groupem.models import Faculty
from django.contrib.auth import authenticate, login


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

def auth(request):
    username = request.POST['username']
    user = authenticate(username=username)
    if user is not None:
#        if user.is_staff:
#            return HttpResponseRedirect('/admin/')
#        else:
        login(request, user)
#            hit_counter = Counter.objects.filter(name='hitcount')[0]
#            hit_counter.count += 1
#            hit_counter.save()
        return HttpResponseRedirect(reverse('bugtracker:choose_role'))
    else:
        if username == "":
            error_message = "You didn't provide a username."
        else:
            error_message = "The user "+username+" does not exist."
        return render(request, 'groupem/index.html',
                      {'error_message': error_message})
