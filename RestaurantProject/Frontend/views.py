from django.shortcuts import render, redirect
from Restaurantapp.models import RestaurantDb, ListRestDb
from Frontend.models import ContactDb, RegUserDb, CartDB, OrderDb
from django.contrib import messages
from RestaurantProject import settings
import razorpay

# Create your views here.


def home_page(request):
    raw = RestaurantDb.objects.all()
    return render(request, "Home.html", {'raw': raw})


def rest_view(request):
    data = ListRestDb.objects.all()
    lis = RestaurantDb.objects.all()
    return render(request, "rest_cat_view.html", {'data': data, 'lis': lis})


def show_cat(request,rest_id):
    show = ListRestDb.objects.filter(Rest_list=rest_id)
    look = RestaurantDb.objects.all()
    return render(request, "rest_show_cat.html", {'show': show, 'look': look})


def single_view_rest(request,code_id):
    data = ListRestDb.objects.get(id=code_id)
    row = RestaurantDb.objects.all()
    return render(request, "single_view.html",{'data': data, 'row':row})


def about_us_page(request):
    about = RestaurantDb.objects.all()
    return render(request, "About_us.html", {'about': about})


def services_page(request):
    now = RestaurantDb.objects.all()
    return render(request, "Services.html", {'asset': now})


def contact_us_page(request):
    con = RestaurantDb.objects.all()
    return render(request, "Contact_us.html", {'con': con})


def save_contact(request):
    if request.method == "POST":
        fna = request.POST.get('first-name')
        lna = request.POST.get('last-name')
        ema = request.POST.get('email')
        adr = request.POST.get('address')
        cit = request.POST.get('city')
        con = request.POST.get('country')
        tel = request.POST.get('tel')
        mes = request.POST.get('message')
        obj = ContactDb(Firstname=fna, Lastname=lna, Email=ema, Address=adr, City=cit, Country=con, Telephone=tel, Message=mes)
        obj.save()
        return redirect(contact_us_page)


def reg_page(request):
    return render(request, "Register.html")


def log_page(request):
    return render(request, "login.html")


def save_reg(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        usn = request.POST.get('username')
        ema = request.POST.get('email')
        pas = request.POST.get('password')
        num = request.POST.get('number')
        obj = RegUserDb(name=nam, username=usn, email=ema, password=pas, number=num)
        obj.save()
        return redirect(log_page)


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegUserDb.objects.filter(username=un, password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            messages.success(request, "Welcome log Successfully!!...")
            return redirect(home_page)
        else:
            messages.error(request, "Invalid Username or password!!...")
            return redirect(log_page)
    else:
        return redirect(log_page)


def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged Out Successfully!!...")
    return redirect(log_page)



def cart_page(request):
    data = CartDB.objects.filter(Username=request.session['username'])
    raw = RestaurantDb.objects.all()
    total_price = 0
    for i in data:
        total_price = total_price+i.Total_price
    return render(request, "Cart.html", {'data': data, 'total_price': total_price, 'raw':raw})


def save_cart(request):
    if request.method == "POST":
        usname = request.POST.get('uname')
        lname = request .POST.get('rtname')
        quan = request.POST.get('quant')
        tprice = request.POST.get('tprc')
        des = request.POST.get('review')
        obj = CartDB(Username=usname, Type_name=lname, Quantity=quan, Total_price=tprice, Review=des)
        obj.save()
        messages.success(request, "Added to Cart Successfully!!...")
        return redirect(cart_page)


def rem_cart(request, dataid):
    van = CartDB.objects.filter(id=dataid)
    van.delete()
    messages.error(request, "Removed from Cart Successfully!!...")
    return redirect(cart_page)


def checkout_page(request):
    raw = RestaurantDb.objects.all()
    info = CartDB.objects.filter(Username=request.session['username'])
    total_cost = 0
    for j in info:
        total_cost = total_cost + j.Total_price
    return render(request, "Checkout.html", {'info': info, 'total_cost': total_cost, 'raw': raw})


def save_check(request):
    if request.method == "POST":
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        mail = request.POST.get('email')
        ad = request.POST.get('address')
        cit = request.POST.get('city')
        con = request.POST.get('country')
        zi = request.POST.get('zip-code')
        tl = request.POST.get('tel')
        obj = OrderDb(First_name=fname, Last_name=lname, E_mail=mail, A_dress=ad, C_ity=cit, Country=con, Zipcode=zi, Tele=tl)
        obj.save()
        messages.success(request, "Order placed Successfully!!...")
        return redirect(home_page)
def payment(request):
    if request.method=="POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_VgBma7PCfLRUjk','x2pkQDpjJR5g8Dq81wnaEy7W'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"pay.html")


