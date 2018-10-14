from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from .filters import UserFilter

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'mysearch/user_list.html', {'filter': user_filter})