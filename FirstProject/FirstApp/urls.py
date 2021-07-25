from django.urls import path
from django.urls.resolvers import URLPattern
from FirstApp import views
from django.contrib.auth import views as v
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnct/',views.contact,name="ct"),
    path('rg/',views.usrreg,name="reg"),
    path('order/',views.order,name="order"),
    path('oc/',views.orderaccept,name="accept"),
    path('od/<int:m>',views.od,name="od"),
    path('additems/',views.additems,name="additems"),
    path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
    path('logout',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
    path('roletype/',views.rolereq,name="rlrq"),
    path('gvper/',views.gveperm,name="gvpm"),
    path('gvup/<int:t>/',views.gvupd,name="gvup"),
    path('gvdel/<int:m>/',views.gvdel,name="gvdel"),
    path('pfle/',views.pfle,name="pf"),
    path('pfupd/',views.pfupd,name="pfupd"),
    path('fbd',views.feedback,name="fd"),
    path('chge/',views.changepwd,name="chpd"),
]