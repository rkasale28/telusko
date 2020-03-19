from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('csignup',views.csignup,name="csignup"),
    path('psignup',views.psignup,name="psignup"),
    path('cform_submit',views.csubmit,name="csubmit"),
    path('pform_submit',views.psubmit,name="psubmit"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('operate',views.operate,name="operate"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)