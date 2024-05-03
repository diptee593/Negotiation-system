from django.urls import path
from userauths.views import *

app_name = "userauths"

urlpatterns = [
    path("", register_view, name="sign-up"),
    path("lognreg", testview2, name="lognreg"),
    path("regis",  testview, name="regis"),
    path("logout",  logout_view, name="logout"),

]