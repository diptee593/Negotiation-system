from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL

# Create your views here.
def register_view(request):
    

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        # print("Registered successfully")
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hello {username}, your account has been created")
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            login(request, new_user)
            return render(request, "Parallel/first.html")
    else:
        print("User can't be registered")
        form = UserRegisterForm()


    context = {
        'form':form
    }

    return render(request, "userauths/sign-up.html", context)


#for registration
def testview(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        # print("Registered successfully")
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hello {username}, your account has been created")
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            login(request, new_user)
            return render(request, "userauths/buyerhome.html")
    else:
        print("User can't be registered")
        form = UserRegisterForm()


    context = {
        'form':form
    }

    # return render(request, "userauths/sign-up.html", context)


    return render(request, "userauths/regspg.html",context)




#for login
def testview2(request):
    if request.user.is_authenticated:
        return render(request, "userauths/buyerhome.html")
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} doesn't exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return render(request, "userauths/buyerhome.html")
        else:
            messages.warning(request, "User doesn't exists.")

    return render(request, "userauths/loginpg.html")



#for logout
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out")
    return render(request, "userauths/loginpg.html")

