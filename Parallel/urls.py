from django.urls import path
from Parallel.views import *

urlpatterns = [
    path('Testing', view1),
    path('mainpg', mainpg),
]