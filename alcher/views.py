from django.shortcuts import render



def homepage(request):
   context={
        'likes':[2,3,7,6,5],
    }
   return render(request,'alcher/homepage.html',context)

def login(request):
  return render(request,'alcher/login.html')
def createpage(request):
  return render(request,'alcher/createpage.html')  
def myposts(request):
     context={
        'likes':[2,3,7,6,5],
    }
     return render(request,'alcher/mypost.html',context)