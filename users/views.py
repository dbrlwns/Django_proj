from django.shortcuts import render

# Create your views here.
def user_auth(request):
    return render(request, 'users/user_auth.html')