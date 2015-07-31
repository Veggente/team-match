        Welcome to Group \'em,
        {% if user.is_authenticated %}
            {% if user.first_name %}
                {{ user.first_name }}.
            {% else %}
                {{ user.username }}.
            {% endif %}
            <a href="{% url 'bugtracker:logout' %}">Logout</a>
        {% else %}
            Guest.
        {% endif %}

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django import template

from bugtracker.models import Counter

register = template.Library()

def get_all_logged_in_users():
    """This function gets the number of logged-in users

    This is given as an answer by T. Stone at
    http://stackoverflow.com/questions/2723052/how-to-get-the-list-of-the-authenticated-users
    """
    # Query all non-expired sessions.
    # Use timezone.now() instead of datatime.now() in
    # latest versions of Django.
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []
    # Build a list of user ids from that query.
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))
    # Query all logged-in users based on id list.
    return User.objects.filter(id__in=uid_list)

@register.inclusion_tag('bugtracker/'
                        'logged_in_user_list.html')
def render_logged_in_user_list():
    hit_counter, created = Counter.objects.get_or_create(
        name='hitcount')
    return {'users': get_all_logged_in_users(), 'hitcount': hit_counter.count}
