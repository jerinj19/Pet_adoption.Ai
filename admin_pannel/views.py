from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from admin_pannel.models import Admin_add


def admin_index(request):
    return render(request, "admin_index.html")
def adminlogin_page(request):
    return render(request,"admin_login.html")

def admin_login(request):
    if request.method == "POST":
        admin_usr = request.POST.get('Admin_username')
        admin_pwd = request.POST.get('admin_password')

        if User.objects.filter(username__contains=admin_usr).exists():
            data = authenticate(username=admin_usr, password=admin_pwd)

            if data is not None:
                login(request, data)
                request.session['username']=admin_usr
                request.session['password']=admin_pwd
                return redirect(admin_index)
            else:
                return redirect(adminlogin_page)

        else:
            return redirect(adminlogin_page)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin_page)

def admin_add(request):
    return render(request,"admin_add.html")
def saveadd(request):
    if request.method=="POST":
        add_name=request.POST.get('ad_name')
        add_location=request.POST.get('ad_location')
        add_images=request.FILES['ad_images']
        obj=Admin_add(Add_name=add_name,Add_location=add_location,Add_images=add_images)
        obj.save()
    return redirect(admin_add)
def viewadd(request):
    add_data=Admin_add.objects.all
    return render(request,"viewadd.html",{'add_data':add_data})
def editadd(request,A_id):
    edit=Admin_add.objects.get(id=A_id)
    return render(request,"edit_add.html",{'edit':edit})
def updateadd(request,u_id):
    if request.method=="POST":
        add_name=request.POST.get('ad_name')
        add_location=request.POST.get('ad_location')
        try:
            img = request.FILES['ad_images']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Admin_add.objects.get(id=u_id).Add_images
        Admin_add.objects.filter(id=u_id).update(
            Add_name=add_name,
            Add_location=add_location,
            Add_images=file
            )
        return redirect(viewadd)

def deleteadd(request,del_id):
    add_delete=Admin_add.objects.filter(id=del_id)
    add_delete.delete()
    return redirect(viewadd)







