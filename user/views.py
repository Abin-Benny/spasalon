from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from hashlib import sha256
from user.models import salonlogin,clientlogin,salonreg,clientreg, salondetails,bookingdetails,reviews,contact
from django.contrib import messages
from datetime import date
import csv
import xlwt

from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail



# Create your views here.

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        icontact = contact()
        icontact.First_name = fname
        icontact.Last_name = lname
        icontact.Email = email
        icontact.Subject = subject
        icontact.Message = message
        icontact.save()
        messages.info(request, "Your Message sent successfully")
        return redirect("index")
    else:
        return render(request,"index.html")

def salon(request):
    sdetails = salondetails.objects.all().exclude(Salon_name="", Opening_hours="", Services="", Service_price="", Address="")
    return render(request, "salon.html", {'sdetails': sdetails})


def salonregister(request):
    if request.method == 'POST':
        sfname = request.POST.get('fname')
        slname = request.POST.get('lname')
        semail = request.POST.get('email')
        spassword = request.POST.get('pass')
        scpassword = request.POST.get('cpass')
        epassword = sha256(spassword.encode()).hexdigest()
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
            sloginobj.Password = epassword
            sloginobj.save()

            ssalondetails = salondetails()
            ssalondetails.Login_id = sloginobj
            ssalondetails.save()

            ssalonreg = salonreg()
            ssalonreg.Login_id = sloginobj
            ssalonreg.First_name = sfname
            ssalonreg.Last_name = slname
            ssalonreg.Email = semail
            ssalonreg.Password = epassword
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
        epassword = sha256(lspassword.encode()).hexdigest()
        print(epassword)
        lsuser = salonlogin.objects.filter(Username=lsusername, Password=epassword)
        if lsuser:
            salonownerdetails = salonlogin.objects.get(Username=lsusername, Password=epassword)
            slid = salonownerdetails.id
            request.session['sid'] = slid
            sdetails=salondetails.objects.get(Login_id=slid)
            if(sdetails.Salon_name==""):
                return redirect('salonowner')
            else:
                return redirect('salonhome')
        else:
            return render(request, "salonlogin.html", {'msg': "Invalid Credentials"})
    else:
        return render(request, "salonlogin.html")


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

        today = date.today()
        datetoday = today.strftime("%m/%d/%Y")
        appnum=bookingdetails.objects.filter(Status="Paid",Date=datetoday,Slid=slid).count()
        booknum = bookingdetails.objects.filter(Slid=slid, Status="Pending").count()
        return render(request, "salonhome.html",{'fsname':fsname,'lsname':lsname,'appnum':appnum,'datetoday':datetoday,'booknum':booknum})
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
        upassword = request.POST.get('pass')
        ucpassword=request.POST.get('cpass')
        epassword = sha256(upassword.encode()).hexdigest()
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
            cloginobj.Password = epassword
            cloginobj.save()

            cuserreg = clientreg()
            cuserreg.Login_id = cloginobj
            cuserreg.First_name = ufname
            cuserreg.Last_name = ulname
            cuserreg.Email = uemail
            cuserreg.Password = epassword
            cuserreg.Mobile = umobile
            cuserreg.Address = uaddress
            cuserreg.save()
            userdetails = clientlogin.objects.get(Username=uemail, Password=epassword)
            cid = userdetails.id
            request.session['cid'] = cid
            return redirect("userhome")

    else:
        return render(request, "userregister.html")

def userlogin(request):
    if request.method == 'POST':
        lcusername=request.POST.get('user')
        lcpassword=request.POST.get('password')
        epassword = sha256(lcpassword.encode()).hexdigest()
        lcuser=clientlogin.objects.filter(Username=lcusername,Password=epassword)
        if lcuser:
            userdetails = clientlogin.objects.get(Username=lcusername, Password=epassword)
            cid = userdetails.id
            request.session['cid'] = cid
            return redirect("userhome")
        else:
            return render(request, "userlogin.html", {'msg': "Invalid Credentials"})
    else:
        return render(request, "userlogin.html")

def userhome(request):
    if 'cid' in request.session:
        id = request.session['cid']
        sdetails = salondetails.objects.all().exclude(Salon_name="", Opening_hours="", Services="", Service_price="", Address="")
        applist = bookingdetails.objects.filter(Lid=id, Status="Confirmed")
        if applist:
            return render(request, "userhomepay.html", {'sdetails': sdetails})
        else:
            return render(request, "userhome.html", {'sdetails': sdetails})
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
        sdetails = salondetails.objects.all().exclude(Salon_name="", Opening_hours="", Services="", Service_price="", Address="")
        applist = bookingdetails.objects.filter(Lid=id, Status="Confirmed")
        if applist:
            return render(request, "userhomepay.html", {'sdetails': sdetails})
        else:
            return render(request, "userhome.html", {'sdetails': sdetails})
    else:
        return redirect("userlogin")

def pay(request,id):
    if 'cid' in request.session:
        clid = request.session['cid']
        return render(request,"bank.html",{'id':id})
    else:
        return redirect("userlogin")

def card(request,id):
    if 'cid' in request.session:
        clid = request.session['cid']
        if request.method == 'POST':
            fullname = request.POST.get('fname')
            cnumber = request.POST.get('cardno')
            cvv = request.POST.get('cvv')
            udetail = bookingdetails.objects.get(id=id, Status="Confirmed")
            udetail.Status = "Paid"
            udetail.save()
            return redirect("userhome")
        else:
            return redirect("card")
    else:
        return redirect("userlogin")

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


def reviewss(request,id):
    if 'cid' in request.session:
        cid = request.session['cid']
        sreviews = reviews.objects.filter(Sid=id)
        return render(request, "reviews.html", {'sreviews': sreviews, 'k': id})
    else:
        return redirect("userlogin")

def addreviews(request,id):
    if 'cid' in request.session:
        cid = request.session['cid']
        sdetails = salondetails.objects.get(Login_id=id)
        sid = sdetails.Login_id.id
        return render(request, "addreview.html", {'sid': sid})
    else:
        return redirect("userlogin")

def submitreviews(request,id):
    if 'cid' in request.session:
        clid = request.session['cid']
        if request.method == 'POST':
            rname= request.POST.get('name')
            rrev= request.POST.get('review')

            reviewform = reviews()
            reviewform.Uid = clid
            reviewform.Sid = id
            reviewform.Name = rname
            reviewform.Review = rrev
            reviewform.save()
            return redirect("userhome")
        else:
            return render(request,"addreview.html")
    else:
        return redirect("userlogin")

def salonappointments(request):
    if 'sid' in request.session:
        id = request.session['sid']
        applist=bookingdetails.objects.filter(Slid=id,Status="Paid")
        return render(request,"salonappointments.html",{'applist':applist})
    else:
        return redirect("salonlogin")

def bookings(request):
    if 'sid' in request.session:
        id = request.session['sid']
        applist=bookingdetails.objects.filter(Slid=id,Status="Pending")
        #num=bookingdetails.objects.filter(Slid=id,Status="Pending").count()
        #print(num)
        return render(request,"bookingstatus.html",{'applist':applist})
    else:
        return redirect("salonlogin")

def todayappointments(request):
    if 'sid' in request.session:
        id = request.session['sid']
        today = date.today()
        datetoday = today.strftime("%m/%d/%Y")
        applist = bookingdetails.objects.filter(Status="Paid", Date=datetoday, Slid=id)
        print(applist)
        for i in applist:
            print(i.Email)
        return render(request,"todayappointment.html",{'applist':applist,'dates':  datetoday})
    else:
        return redirect("salonlogin")

def exportcsv(request):
    if 'sid' in request.session:
        id = request.session['sid']
        today = date.today()
        datetoday = today.strftime("%m/%d/%Y")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition']='Attachment:filename= todaysappointments'+str(datetoday)+'.csv'
        writer=csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Mobile', 'Service', 'Time', 'Status'])
        applist = bookingdetails.objects.filter(Status="Paid", Date=datetoday, Slid=id)
        for i in applist:
            writer.writerow([i.First_name,i.Last_name,i.Email,i.Mobile,i.Services,i.Time,i.Status])
        return response

def exportexcel(request):
    if 'sid' in request.session:
        id = request.session['sid']
        today = date.today()
        datetoday = today.strftime("%m/%d/%Y")
        #applist = bookingdetails.objects.filter(Status="Paid", Date=datetoday, Slid=id)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="todaysappointments.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Todays Appointments')  # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['First Name', 'Last Name', 'Email', 'Mobile', 'Services', 'Time', 'Status', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = bookingdetails.objects.filter(Status="Paid", Date=datetoday, Slid=id).values_list('First_name', 'Last_name', 'Email', 'Mobile', 'Services', 'Time', 'Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)


        wb.save(response)

        return response

def exportpdf(request):
    if 'sid' in request.session:
        id = request.session['sid']
        today = date.today()
        datetoday = today.strftime("%m/%d/%Y")
        sname= salondetails.objects.filter(Login_id=id)
        for i in sname:
            salonname=i.Salon_name
        applist =  bookingdetails.objects.filter(Status="Paid", Date=datetoday, Slid=id)

        template_path = 'pdf.html'
        context = {'applist': applist,'dates':datetoday,'salonname':salonname}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # If you  don't want to download it directly or you want to view the pdf then download it,use below code
        response['Content-Disposition'] = 'filename="report.pdf"'
        #If you want to download it directly,use below code
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response



def payment(request):
    if 'cid' in request.session:
        clid = request.session['cid']
        applist=bookingdetails.objects.filter(Lid=clid,Status="Confirmed")
        return render(request,"userbookings.html",{'applist':applist})
    else:
        return redirect("userlogin")

def user_forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        print(email)
        cuser = clientreg.objects.filter(Email=email)
        if cuser:
            subject = "Password Reset Link"
            msg = "Dear Customer,Click this link http://127.0.0.1:8000/User/Forgot_Password_Reset to reset your password"
            to = email
            send_mail(subject, msg, settings.EMAIL_HOST_USER, [to], fail_silently = False)
            return render(request, "forgot_password.html", {'msg': "Password Reset Link sent to Your Registered Email ID.Please check your Email"})

        else:
            return render(request, "forgot_password.html",{'msg': "Entered Username is not registered.Please check your Username"})
    else:
        return render(request, "forgot_password.html")
def user_forgot_password_reset(request):
    if request.method == 'POST':
        print("hi")
        femail = request.POST.get('email')
        print(femail)
        fpassword = request.POST.get('pass')
        print(fpassword)
        fepassword = sha256(fpassword.encode()).hexdigest()
        fcpassword = request.POST.get('cpass')
        print(fcpassword)
        if (fpassword != fcpassword):
            messages.info(request, "Password Doesn't Match")
            return redirect('ufpasswordreset')
        else:
            detail = clientreg.objects.filter(Email=femail)
            for i in detail:
                i.Password = fepassword
                i.save()
            details = clientlogin.objects.filter (Username=femail)
            for x in details:
                x.Password = fepassword
                x.save()
            return redirect("userlogin")
    else:
        return render(request, "password_reset.html")


def salon_forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        print(email)
        cuser = salonreg.objects.filter(Email=email)
        if cuser:
            subject = "Password Reset Link"
            msg = "Dear Salon Owner,Click this link http://127.0.0.1:8000/Salon/Forgot_Password_Reset to reset your password"
            to = email
            send_mail(subject, msg, settings.EMAIL_HOST_USER, [to], fail_silently = False)
            return render(request, "salon_forgot_password.html", {'msg': "Password Reset Link sent to Your Registered Email ID.Please check your Email"})

        else:
            return render(request, "salon_forgot_password.html",{'msg': "Entered Username is not registered.Please check your Username"})
    else:
        return render(request, "salon_forgot_password.html")
def salon_forgot_password_reset(request):
    if request.method == 'POST':
        femail = request.POST.get('email')
        fpassword = request.POST.get('pass')
        fepassword = sha256(fpassword.encode()).hexdigest()
        fcpassword = request.POST.get('cpass')

        if (fpassword != fcpassword):
            messages.info(request, "Password Doesn't Match")
            return redirect('sfpasswordreset')
        else:
            detail = salonreg.objects.filter(Email=femail)
            for i in detail:
                i.Password = fepassword
                i.save()
            details = salonlogin.objects.filter (Username=femail)
            for x in details:
                x.Password = fepassword
                x.save()
            return redirect("salonlogin")
    else:
        return render(request, "salon_password_reset.html")




def logouts(request):
    logout(request)
    return redirect("index")






































































































































































































































































