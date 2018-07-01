from django.shortcuts import render
from .models import clubs,club_members
# Create your views here.
def club(request):
	return render(request,'recruitment/clubs.html')
def resume_ie(request):
	return render(request,'recruitment/resume_form.html')
def resume_ieee(request):
	return render(request,'recruitment/resume_ieee.html')
def resume_acm(request):
	return render(request,'recruitment/resume_acm.html')
def resume_rotaract(request):
	return render(request,'recruitment/resume_rotaract.html')
def resume_iet(request):
	return render(request,'recruitment/resume_iet.html')
def resume_iste(request):
	return render(request,'recruitment/resume_iste.html')
def result(request):
	return render(request,'recruitment/result1.html')
def logged_in(request):
	#club=clubs.objects.all()
	club=clubs.objects.get(club_id=request.POST['club_id'])
	userid=request.POST.get('user_id')
	password=request.POST.get('pass')
	try:
		user=club.club_members_set.get(user_id=userid, Password=password)
	except(KeyError,club_members.DoesNotExist):
		return render(request,'recruitment/member.html',{'error':"user Not FOund"})
	return render(request,'recruitment/member.html',{'Name':user.Name,'Rollno':user.Rollno})