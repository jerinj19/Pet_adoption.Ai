from django.shortcuts import render

def index_admin(request):
    return render(request,"index.html")
def about(request):
    return render(request,"contact.html")
