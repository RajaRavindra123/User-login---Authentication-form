from . import views
from django.urls import path,include
from . import views
#from . import force_bytes, force_str

urlpatterns = [
    path("",views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]