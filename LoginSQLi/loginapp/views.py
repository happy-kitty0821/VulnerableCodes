from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'index.html')


from django.shortcuts import render
from .models import User

def login(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']

        user = User()
        result = user.authenticate_user(input_username, input_password)

        if result:
            # Authentication successful
            return render(request, 'success.html')
        else:
            # Authentication failed
            return render(request, 'failure.html')
    return render(request, 'login.html')
