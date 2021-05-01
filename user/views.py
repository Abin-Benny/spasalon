from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from user.models import salonlogin,clientlogin,salonreg,clientreg, salondetails,bookingdetails
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")

def salonregister(request):
    if request.method == 'POST':
        sfname = request.POST.get('fname')
        slname = request.POST.get('lname')
        semail = request.POST.get('email')
        spassword = request.POST.get('password')
        scpassword = request.POST.get('cpassword')
        smobile = request.POST.get('mobile')
        saddress = request.POST.get('address')

        if (salonreg.objects.filter(Email=semail).exists()):
            messages.info(request, "Email ID Already Taken")
            return redirect('salonregister')

        elif (spassword != scpassword):
            messages.info(request, "Password Doesn't Match")
            return redirect('salonregister')

        elif (salonreg.objects.filter(Mobile=smobile).exists()):
            messages.info(request, "Mobile Number Already Taken")
            return redirect('salonregister')

        else:
            sloginobj = salonlogin()
            sloginobj.Username = semail
            sloginobj.Password = spassword
            sloginobj.save()

            ssalondetails = salondetails()
            ssalondetails.Login_id = sloginobj
            ssalondetails.save()

            ssalonreg = salonreg()
            ssalonreg.Login_id = sloginobj
            ssalonreg.First_name = sfname
            ssalonreg.Last_name = slname
            ssalonreg.Email = semail
            ssalonreg.Password = spassword
            ssalonreg.Mobile = smobile
            ssalonreg.Address = saddress
            ssalonreg.save()
            ssalondetail = salonreg.objects.get(Email=semail)
            slid = ssalondetail.id
            fsname = ssalondetail.First_name
            lsname = ssalondetail.Last_name
            request.session["sid"] = slid
            return render(request, "salonowner.html", {'fsname': fsname , 'lsname': lsname})

    else:
        return render(request, "salonregister.html")

def salonlogins(request):
    if request.method == 'POST':
        lsusername = request.POST.get('user')
        lspassword = request.POST.get('password')
        lsuser = salonlogin.objects.filter(Username=lsusername, Password=lspassword)
        if lsuser:
            salonownerdetails = salonlogin.objects.get(Username=lsusername, Password=lspassword)
            slid = salonownerdetails.id
            request.session['sid'] = slid
            sdetails=salondetails.objects.get(Login_id=slid)
            if(sdetails.Salon_name==""):
                return redirect('salonowner')
            else:
                return redirect('salonhome')
        else:
            return render(request, "salon_login.html", {'msg': "Invalid Credentials"})
    else:
        return render(request, "salon_login.html")


def salonowner(request):
    if 'sid' in request.session:
        slid = request.session['sid']
        detail=salonreg.objects.get(id=slid)
        fsname=detail.First_name
        lsname=detail.Last_name
        return render(request, "salonowner.html",{'fsname':fsname,'lsname':lsname})
    else:
        return redirect("salonlogin")

def salonhome(request):
    if 'sid' in request.session:
        slid = request.session['sid']
        detail = salonreg.objects.get(id=slid)
        fsname = detail.First_name
        lsname = detail.Last_name
        return render(request, "salonhome.html",{'fsname':fsname,'lsname':lsname})
    else:
        return redirect("salonlogin")

def addsalon(request):
    if 'sid' in request.session:
        slid = request.session['sid']
        if request.method == 'POST':
            sname = request.POST.get('salonname')
            ohours = request.POST.get('openinghours')
            sservices = request.POST.get('services')
            sserviceprice = request.POST.get('serviceprice')
            if len(request.FILES) != 0:
                simg = request.FILES['image']
            else:
                simg = 'images/default.jpg'
            saddress = request.POST.get('address')

            ssalondetails = salondetails.objects.filter(Login_id=slid)
            for i in ssalondetails:
                i.Salon_name = sname
                i.Opening_hours = ohours
                i.Services = sservices
                i.Service_price = sserviceprice
                i.Image = simg
                i.Address = saddress
                i.save()

            return redirect("salonhome")
        else:
            return render(request, "addsalon.html")
    else:
        return redirect("salonlogin")


def updatesalon(request):
    if 'sid' in request.session:
        slid = request.session['sid']
        if request.method == 'POST':
            uname = request.POST.get('salonname')
            uohours = request.POST.get('openinghours')
            usservices = request.POST.get('services')
            usserviceprice = request.POST.get('serviceprice')
            if len(request.FILES) != 0:
                usimg = request.FILES['image']
            else:
                usimg = 'images/default.jpg'
            usaddress = request.POST.get('address')

            udetail = salondetails.objects.filter(Login_id=slid)
            for i in udetail:
                i.Salon_name = uname
                i.Opening_hours = uohours
                i.Services = usservices
                i.Service_price = usserviceprice
                if len(request.FILES) != 0:
                    i.Image = usimg
                i.Address = usaddress
                i.save()
            return redirect("salonhome")
        else:
            udetail = salondetails.objects.filter(Login_id=slid)
            return render(request, "updatesalon.html", {'udetail': udetail})
    else:
        return redirect("salonlogin")

def userregister(request):
    if request.method == 'POST':
        ufname = request.POST.get('fname')
        ulname = request.POST.get('lname')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        ucpassword=request.POST.get('cpassword')
        umobile = request.POST.get('mobile')
        uaddress = request.POST.get('address')

        if (clientreg.objects.filter(Email=uemail).exists()):
            messages.info(request, "Email ID Already Taken")
            return redirect('userregister')
        elif (upassword!=ucpassword):
            messages.info(request, "Password Doesn't Match")
            return redirect('userregister')
        elif (clientreg.objects.filter(Mobile=umobile).exists()):
            messages.info(request, "Mobile Number Already Taken")
            return redirect('userregister')

        else:
            cloginobj = clientlogin()
            cloginobj.Username = uemail
            cloginobj.Password = upassword
            cloginobj.save()

            cuserreg = clientreg()
            cuserreg.Login_id = cloginobj
            cuserreg.First_name = ufname
            cuserreg.Last_name = ulname
            cuserreg.Email = uemail
            cuserreg.Password = upassword
            cuserreg.Mobile = umobile
            cuserreg.Address = uaddress
            cuserreg.save()
            userdetails = clientlogin.objects.get(Username=uemail, Password=upassword)
            cid = userdetails.id
            request.session['cid'] = cid
            return redirect("userhome")

    else:
        return render(request, "userregister.html")

def userlogin(request):
    if request.method == 'POST':
        lcusername=request.POST.get('user')
        lcpassword=request.POST.get('password')
        lcuser=clientlogin.objects.filter(Username=lcusername,Password=lcpassword)
        if lcuser:
            userdetails = clientlogin.objects.get(Username=lcusername, Password=lcpassword)
            cid = userdetails.id
            request.session['cid'] = cid
            return redirect("userhome")
        else:
            return render(request, "user_login.html", {'msg': "Invalid Credentials"})
    else:
        return render(request, "user_login.html")

def userhome(request):
    if 'cid' in request.session:
        id = request.session['cid']
        sdetails = salondetails.objects.all()
        #applist = bookingdetails.objects.filter(Lid=id, Status="Confirm")
        return render(request, "userhome.html", {'sdetails': sdetails})
        '''if applist:
            applist = bookingdetails.objects.filter(Lid=id, Status="Confirm")
            for s in applist:
                k = s.Lid
                return render(request, "userhomepay.html", {'sdetails': sdetails, 'k': k})

        else:
            return render(request, "userhome.html", {'sdetails': sdetails})'''
    else:
        return redirect("userlogin")

def booking(request,id):
    if 'cid' in request.session:
        cid = request.session['cid']
        sdetails = salondetails.objects.get(Login_id=id)
        serve = sdetails.Services
        sid = sdetails.Login_id.id
        if ',' in serve:
            opserve = serve.split(',')
            return render(request, "booking.html", {'opserve': opserve, 'sid': sid})
        else:
            return render(request, "booking.html", {'oneserve': serve, 'sid': sid})
    else:
        return redirect("userlogin")

def appsubmit(request,id):
    if 'cid' in request.session:
        clid = request.session['cid']
        if request.method == 'POST':
            afname = request.POST.get('fname')
            alname = request.POST.get('lname')
            aemail = request.POST.get('email')
            amobile = request.POST.get('mobile')
            aserve = request.POST.get('service')
            adate = request.POST.get('dates')
            atime = request.POST.get('times')

            appdetails = bookingdetails()
            appdetails.Lid = clid
            appdetails.Slid = id
            appdetails.First_name = afname
            appdetails.Last_name = alname
            appdetails.Email = aemail
            appdetails.Mobile = amobile
            appdetails.Services = aserve
            appdetails.Date = adate
            appdetails.Time = atime
            appdetails.Status = "Pending"
            appdetails.save()
            return redirect("userhome")
    else:
        return redirect("userlogin")

def userhomepay(request):
    if 'cid' in request.session:
        id = request.session['cid']
        sdetails = salondetails.objects.all()
        applist = bookingdetails.objects.filter(Lid=id, Status="Confirm")
        if applist:
            '''applist = bookingdetails.objects.filter(Lid=id, Status="Confirm")
            for s in applist:
                k = s.Lid'''
            return render(request, "userhomepay.html", {'sdetails': sdetails})
        else:
            return render(request, "userhome.html", {'sdetails': sdetails})
    else:
        return redirect("userlogin")

def payment(request):
    if 'cid' in request.session:
        clid = request.session['cid']
        applist=bookingdetails.objects.filter(Lid=clid,Status="Confirm")
        return render(request,"userbookings.html",{'applist':applist})
    else:
        return redirect("userlogin")

def pay(request):
    if 'cid' in request.session:
        clid = request.session['cid']
        return render(request,"bank.html")
    else:
        return redirect("userlogin")

def bookings(request):
    if 'sid' in request.session:
        id = request.session['sid']
        applist=bookingdetails.objects.filter(Slid=id,Status="Pending")
        #num=bookingdetails.objects.filter(Slid=id,Status="Pending").count()
        #print(num)
        return render(request,"bookingstatus.html",{'applist':applist})
    else:
        return redirect("salonlogin")

def statusupdate(request,ids):
    if 'sid' in request.session:
        id = request.session['sid']
        if request.method == 'POST':
            sstatus = request.POST.get('status')

            udetail = bookingdetails.objects.get(id=ids,Status="Pending")
            udetail.Status = sstatus
            udetail.save()
            return redirect("bookings")
        else:
            udetail = bookingdetails.objects.get(id=ids,Status="Pending")
            uid=udetail.id
            return render(request, "statusupdate.html", {'uid': uid})
    else:
        return redirect("salonlogin")



def logouts(request):
    logout(request)
    return redirect("index")