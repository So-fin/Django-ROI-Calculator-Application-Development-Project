from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ContactUs/goToHome/',views.goToHome,name='goToHome'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('ContactUs/', views.ContactUs, name='contactUs'),
    path('index/', views.index, name='index'),
    path('schemes/', views.schemes, name='schemes'),
    path('gold/<int:amount>/<int:duration>', views.gold, name='gold'),
    path('ppf/<int:amount>/<int:duration>', views.ppf, name='ppf'),
    path('fd/<int:amount>/<int:duration>', views.fd, name='fd'),
    path('nsc/<int:amount>/<int:duration>', views.nsc, name='nsc'),
    path('elss/<int:amount>/<int:duration>', views.elss, name='elss'),
    path('emf/<int:amount>/<int:duration>', views.emf, name='emf'),
    path('renderresult/', views.renderresult, name='renderresult'),
    path('index/passdata', views.passdata, name='passdata'),
]
