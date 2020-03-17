from django.urls import path
from . import views

urlpatterns=[
    path('csignup',views.csignup,name="csignup"),
    path('psignup',views.psignup,name="psignup"),
    path('cform_submit',views.csubmit,name="csubmit"),
    path('pform_submit',views.psubmit,name="psubmit"),
]