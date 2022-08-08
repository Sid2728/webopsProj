from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def login(request):
  return render(request,'alcher/login.html')
def logout(request):
  return render(request, 'alcher/logout.html')
@login_required
def homepage(request):
   context={
        'likes':[2,3,7,6,5],
    }
   return render(request,'alcher/homepage.html',context)

@login_required
def myposts(request):
     context={
        'likes':[2,3,7,6,5],
    }
     return render(request,'alcher/mypost.html',context)

@login_required
def createpost(request):
    return render(request ,'alcher/createpage.html')