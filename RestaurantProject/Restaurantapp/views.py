from django.shortcuts import render, redirect
from Restaurantapp.models import RestaurantDb, ListRestDb
from Frontend.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def intro_index_page(request):
    return render(request, "index.html")


def add_restaurant_page(request):
    return render(request, "AddRestaurant.html")


def save_restaurant(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pla = request.POST.get('place')
        star = request.POST.get('star')
        rat = request.POST.get('rate')
        des = request.POST.get('description')
        ph = request.POST.get('contact')
        img = request.FILES['image']
        obj = RestaurantDb(Rest_name=na, Place=pla, Star_rating=star, Rate=rat, Description=des, Contact_No=ph, Image=img)
        obj.save()
        messages.success(request, "Category Added Successfully!!...")
        return redirect(add_restaurant_page)


def display_restaurant(request):
    disp = RestaurantDb.objects.all()
    return render(request, "DisplayRestaurant.html", {'disp': disp})


def edit_restaurant(request, dataid):
    edit = RestaurantDb.objects.get(id=dataid)
    return render(request, "EditRestaurant.html", {'edit': edit})


def update_restaurant(request, dataid):
    if request.method == "POST":
        nam = request.POST.get('name')
        pl = request.POST.get('place')
        sta = request.POST.get('star')
        ra = request.POST.get('rate')
        de = request.POST.get('description')
        phn = request.POST.get('contact')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = RestaurantDb.objects.get(id=dataid).Image
        RestaurantDb.objects.filter(id=dataid).update(Rest_name=nam, Place=pl, Star_rating=sta, Rate=ra, Description=de, Contact_No=phn, Image=file)
        messages.success(request, "Category Edited Successfully!!...")
        return redirect(display_restaurant)


def remv_restaurant(request, dataid):
    re = RestaurantDb.objects.filter(id=dataid)
    re.delete()
    messages.error(request, "Deleted Successfully!!...")
    return redirect(display_restaurant)


def add_rest_det(request):
    rest = RestaurantDb.objects.all()
    return render(request, "AddRestaurantDetails.html", {'rest': rest})


def save_rest_det(request):
    if request.method == "POST":
        rli = request.POST.get('restlist')
        rtp = request.POST.get('rtype')
        bran = request.POST.get('branches')
        cos = request.POST.get('cost')
        rev = request.POST.get('review')
        img = request.FILES['image']
        obj = ListRestDb(Rest_list=rli, Rest_type=rtp, Branches=bran, Cost=cos, Review=rev, Res_img=img)
        obj.save()
        messages.success(request, "Product Added Successfully!!...")
        return redirect(add_rest_det)


def disp_rest_list(request):
    display = ListRestDb.objects.all()
    return render(request, "Display_list_rest.html", {'display': display})


def edit_rest(request, res_id):
    res = RestaurantDb.objects.all()
    item = ListRestDb.objects.get(id=res_id)
    return render(request, "Edit_list_rest.html", {'res': res, 'item': item})


def update_rest(request, dataid):
    if request.method == "POST":
        rlist = request.POST.get('restlist')
        rtype = request.POST.get('rtype')
        branch = request.POST.get('branches')
        co = request.POST.get('cost')
        rev = request.POST.get('review')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)

        except MultiValueDictKeyError:
            file = ListRestDb.objects.get(id=dataid).Res_img
        ListRestDb.objects.filter(id=dataid).update(Rest_list=rlist, Rest_type=rtype, Branches=branch, Cost=co, Review=rev, Res_img=file)
        messages.success(request, "Product Edited Successfully!!...")
        return redirect(disp_rest_list)


def remv_rest(request, dataid):
    remo = ListRestDb.objects.filter(id=dataid)
    remo.delete()
    messages.error(request, "Proudct Deleted Successfully!!...")
    return redirect(disp_rest_list)


def admin_login(request):
    return render(request, "Admin_login.html")


def adminlogin(request):
    if request.method == "POST":
        usn = request.POST.get('user_name')
        psw = request.POST.get('pass_word')
        if User.objects.filter(username__contains=usn).exists():
            conf = authenticate(username=usn, password=psw)
            if conf is not None:
                login(request, conf)
                request.session['username'] = usn
                request.session['password'] = psw
                messages.success(request, "Admin logged in  Successfully!!...")
                return redirect(intro_index_page)

            else:
                messages.error(request, "Invalid Username or password ")
                return redirect(admin_login)

        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged out Successfully!!...")
    return redirect(admin_login)


def user_details(request):
    det = ContactDb.objects.all()
    return render(request, "Usedetails.html", {'det': det})


def cnc_det(request, dlid):
    cnc = ContactDb.objects.filter(id=dlid)
    cnc.delete()
    messages.error(request, "Details Deleted Successfully!!...")
    return redirect(user_details)




