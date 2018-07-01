from django.urls import path
from . import views

urlpatterns=[
	path('',views.club,name='club'),
    path('resume_ie',views.resume_ie,name='resume_ie'),
    path('resume_ieee',views.resume_ieee,name='resume_ieee'),
    path('resume_rotaract',views.resume_rotaract,name='resume_rotaract'),
    path('resume_acm',views.resume_acm,name='resume_acm'),
    path('resume_iste',views.resume_iste,name='resume_iste'),
    path('resume_iet',views.resume_iet,name='resume_iet'),
    path('logged_in',views.logged_in,name='logged_in'),
    path('result',views.result,name='result'),
]