from django.urls import path, include
from accounts.views import login



# сайт/account/
urlpatterns = [
    path('login/', login, name='login'),
]