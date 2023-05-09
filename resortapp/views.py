from datetime import datetime

from django.conf.global_settings import DATE_FORMAT
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Sum, Avg, Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def login1(request):
    return  render(request,'Admin_login page.html')
def Admin_home_page(request):
    return render(request,'Admin_Home_Page.html')
def add_employees(request):
    return  render(request,'Admin_add employee.html')
def add_events(request):
    return  render(request,'Admin_add events.html')
def add_facilities(request):
    return render(request,'Admin_add facility.html')
def add_offers(request):
    ob=package.objects.all()
    return render(request,'Admin_add offers.html',{'val':ob,'cdt':cdate})
def add_packages(request):
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate, "======")
    return render(request,'Admin_add packages.html',{'cdt':cdate})
def add_rooms(request):
    ob=cottage.objects.all()
    return render(request,'Admin_add Room.html',{'val':ob})
def approve_reject_leave(request):
    ob=leave.objects.all()
    return render(request,'Admin_approve_reject leave.html',{'val':ob})
def manage_booking_info(request):
    ob=booking.objects.all()
    return render(request,'Admin_manage booking info.html',{'val':ob})
def manage_employee(request):
    ob=employee.objects.all()
    return render(request,'Admin_Manage employee.html',{'val':ob})
def manage_events(request):
    ob=events.objects.all()
    return render(request,'Admin_manage events.html',{'val':ob})
def manage_facilities(request):
    ob=facilities.objects.all()
    return render(request,'Admin_manage facility.html',{'val':ob})
def manage_offers(request):
    ob=offers.objects.all()
    return render(request,'Admin_manage offers.html',{'val':ob})
def manage_package(request):
    ob=package.objects.all()
    return render(request,'Admin_manage packages.html',{'val':ob})
def manage_purchase_det(request):
    ob=request_materials.objects.all()
    return render(request,'Admin_manage purchase det.html',{'val':ob})
def manage_rooms(request):
    ob=room.objects.all()
    return render(request,'Admin_Manage rooms.html',{'val':ob})
def reason_leave(request):
    return render(request,'Admin_reason_leave.html')
def view_feedback_rating(request):
    ob=feedback.objects.all()
    return render(request,'Admin_view feedback rating.html',{'val':ob})
def view_users(request):
    ob=registration.objects.all()
    return render(request,'Admin_view users.html',{'val':ob})
def view_reports_resort(request):
    return render(request,'Admin_resort_report_.html')
def view_attendance(request):
    return render(request,'Admin_view_attendance.html')
def users_booking_report(request):
    return render(request,'Admin_users_booking_report.html')
def employee_salary(request):
    return render(request,'Admin_emp_salary.html')
def view_cottage(request):
    ob = cottage.objects.all()
    return render(request,'Admin_view_cottage.html',{'val':ob})
def add_cottage(request):
    return render(request,'Admin_add_cottages.html')
def addbutton(request):
    return render(request,'Admin_add_cottages.html')

#############################
def admin_update_room_status(request):
    return render(request,'admin_update_room_availability.html')
def search_room_status(request):
    vdate = request.POST['textfield']
    ob = booking.objects.filter(date_vaccate=vdate)
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate,"======")
    return render(request,'admin_update_room_availability.html',{'v':ob,'date':vdate,'cdt':cdate})
def available_status(request,id):
    ob = room.objects.get(id=id)
    ob.status='available'
    ob.save()
    return HttpResponse('''<script>alert("status updated");window.location="/admin_update_room_status"</script>''')
def manage_event_booking(request):
    ob = event_book.objects.all()
    return render(request, 'Admin_Manage_Events_book.html',{'val':ob})
def search_attendance(request):
    mnth = request.POST['select']
    btn=request.POST['Submit']
    if btn == "SEARCH":
        ob1 = attendance.objects.filter(date__month=mnth).values('date').distinct()
        print(ob1.count(),"*********")
        ob = attendance.objects.filter(date__month=mnth).values('employee_id').annotate(Sum('attendance'),Avg('attendance'))
        print(ob,"=obbbbbbb==================")
        obb=attendance.objects.filter(date__month=mnth).values('employee_id__firstname','employee_id__lastname').annotate(total=Count('attendance'))
        print(obb,"obbbbbbbbbbbbbbbb")
        a=[]
        for i in ob:
            att=i['attendance__sum']/ob1.count() * 100
            print(att,"==============================")
            a.append(att)
        print(a,"********************************")
        results=[]
        for i in range(0,len(a)):
            row={'employee_id__firstname': obb[i]['employee_id__firstname'], 'employee_id__lastname': obb[i]['employee_id__lastname'], 'total': obb[i]['total'],"p":a[i]}
            results.append(row)
        print(obb)
        return render(request, 'Admin_view_attendance.html', {'val': results,'v':ob1.count(),'per':a,'mnth':int(mnth)})
    else:
        return render(request, 'Admin_add_attandence.html')

def add_attendance(request):
    date=request.POST['date']
    btn=request.POST['Submit']
    if btn == 'Search':
        ob=employee.objects.all()
        request.session['date']=date
        return render(request, 'Admin_add_attandence.html',{'v':ob,'date':date})
    else:
        try:
            ee = attendance.objects.filter(date=request.session['date'])
            print(ee,"======")
            if len(ee)==0:
                eid = request.POST.getlist('checks[]')
                for i in eid:
                        ob = attendance()
                        ob.date = request.session['date']
                        ob.attendance = '1'
                        eob = employee.objects.get(loginid__id=i)
                        ob.employee_id = eob
                        ob.save()
                return HttpResponse('''<script>alert("Successfully added");window.location="/view_attendance"</script>''')
            else:
                return HttpResponse('''<script>alert("Already marked");window.location="/view_attendance"</script>''')
        except:
            return HttpResponse('''<script>alert("Already marked");window.location="/view_attendance"</script>''')

# showing booking status and purchase info when we approved
def manage_booking_info_status(request):
    ob = booking.objects.all()
    return render(request, 'Admin_manage booking info.html',{'val':ob})
def manage_purchase_det_status(request):
    ob = request_materials.objects.all()
    return render(request, 'Admin_manage purchase det.html', {'val': ob})
def manage_leave_request(request):
    ob = leave.objects.all()
    return render(request, 'Admin_approve_reject leave.html', {'val': ob})

def search(request):
    type=request.POST['select']
    btn=request.POST['Submit']
    if btn =="SEARCH":
        ob=employee.objects.filter(emptype=type)
        return render(request,'Admin_Manage employee.html',{'val':ob})
    else:
        return render(request, 'Admin_add employee.html')

def deleteemp(request,id):
    ob=employee.objects.get(loginid=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_employee"</script>''')
def deleteeve(request,id):
    ob = events.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_events"</script>''')

def deletefac(request,id):
    ob = facilities.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_facilities"</script>''')

def deleteoff(request,id):
    ob = offers.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_offers"</script>''')

def deletepack(request,id):
    ob = package.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_package"</script>''')

def deleteroom(request,id):
    ob = room.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_rooms"</script>''')

def deletecott(request,id):
    ob = cottage.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/view_cottage"</script>''')


def editemployee (request,id):
    request.session['lid']=id
    ob = employee.objects.get(loginid=id)
    return render(request,'Admin_edit_employee.html',{'val':ob})

def editevent (request,id):
    request.session['lid'] = id
    ob = events.objects.get(id=id)
    return render(request,'Admin_edit_event.html',{'val':ob})

def editfacility (request,id):
    request.session['lid'] = id
    ob = facilities.objects.get(id=id)
    return render(request,'Admin_edit_facility.html',{'val':ob})

def editoffers (request,id):
    request.session['lid'] = id
    ob = offers.objects.get(id=id)
    ob1= package.objects.all()
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate, "======")
    return render(request,'Admin_edit_offers.html',{'val':ob,'val1':ob1,'cdt':cdate})

def editpack (request,id):
    request.session['lid'] = id
    ob = package.objects.get(id=id)
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate, "======")
    return render(request,'Admin_edit_package.html',{'val':ob,'cdt':cdate})

def editroom (request,id):
    request.session['lid'] = id
    ob = room.objects.get(id=id)
    ob1 = cottage.objects.all()
    return render(request,'Admin_edit_rooms.html',{'val':ob,'val1':ob1})

def editcottage (request,id):
    request.session['lid'] = id
    ob = cottage.objects.get(id=id)
    return render(request,'Admin_edit_cottages.html',{'val':ob})

def approve_book_det(request,id):
    ob = booking.objects.get(id=id)
    ob.status = 'accept'
    ob.save()
    return HttpResponse('''<script>alert("Approved");window.location="/manage_booking_info"</script>''')

def reject_book_det(request,id):
    ob = booking.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/manage_booking_info"</script>''')

def approve_purchase_det(request,id):
    ob = request_materials.objects.get(id=id)
    ob.status = 'accept'
    ob.save()
    return HttpResponse('''<script>alert("Approved");window.location="/manage_purchase_det_status"</script>''')

def reject_purchase_det(request,id):
    ob = request_materials.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/manage_purchase_det_status"</script>''')

def approve_leave_req(request,id):
    ob = leave.objects.get(id=id)
    ob.status = 'accept'
    ob.save()
    return HttpResponse('''<script>alert("Approved");window.location="/approve_reject_leave"</script>''')

def reject_leave_req(request,id):
    ob = leave.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/approve_reject_leave"</script>''')

def approve_eve_book (request,id):
    ob = event_book.objects.get(id=id)
    ob.status = 'accept'
    ob.save()
    return HttpResponse('''<script>alert("Approved");window.location="/manage_event_booking"</script>''')

def reject_eve_book(request,id):
    ob = event_book.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/manage_event_booking"</script>''')

def admbooking(request):
    ob = booking.objects.all()
    return render(request, 'Admin_manage booking info.html', {'val': ob})

def fdpaymnt(request):
    ob = menu_orders.objects.all()
    return render(request, 'Admin_food_pydet.html',{'val':ob})

def loginbtn(request):
    uname=request.POST['textfield']
    passwd=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=passwd)
        if ob.type=="admin":
            return redirect("/Admin_home_page")
        elif ob.type=="user":
            request.session['lid']=ob.id
            return redirect("/user_home")
        elif ob.type == "employee":
            request.session['lid'] = ob.id
            obb=employee.objects.get(loginid__id=ob.id)
            if obb.emptype == "KITCHEN" :
                return redirect("/emp_kitchen_home")
            else:
                return redirect("/emp_room_home")
        else:
            return HttpResponse('''<script>alert("invalid username or Password");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location="/"</script>''')


def add_emp(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    places=request.POST['textfield3']
    streets=request.POST['textfield4']
    pincod=request.POST['textfield5']
    cityy=request.POST['textfield6']
    districts=request.POST['select']
    states=request.POST['textfield7']
    mob=request.POST['textfield8']
    gendr=request.POST['radiobutton']
    dob=request.POST['textfield9']
    adarnum=request.POST['textfield14']
    salaries=request.POST['textfield10']
    empltype=request.POST['select2']
    jobtitl=request.POST['textfield11']
    pic = request.FILES['file']
    fn = FileSystemStorage()
    fs = fn.save(pic.name, pic)
    usname=request.POST['textfield12']
    paswrd=request.POST['textfield13']


    lob=login()
    lob.username=usname
    lob.password=paswrd
    lob.type='employee'
    lob.save()

    eob=employee()
    eob.firstname=fname
    eob.lastname=lname
    eob.place=places
    eob.street=streets
    eob.city=cityy
    eob.pincode=pincod
    eob.state=states
    eob.district=districts
    eob.phone=mob
    eob.gender=gendr
    eob.adarnumber=adarnum
    eob.salary=salaries
    eob.emptype=empltype
    eob.jobtitle=jobtitl
    eob.photo=fs
    eob.dob=dob
    eob.loginid=lob
    eob.save()
    return HttpResponse('''<script>alert("Successfully Added New Employee");window.location="/manage_employee"</script>''')

def add_room(request):
    try:
        cott_num=request.POST['select1']
        room_num=request.POST['textfield2']
        nofper=request.POST['textfield3']
        pic=request.FILES['file']
        fn=FileSystemStorage()
        fs=fn.save(pic.name,pic)
        r_facility=request.POST['select']
        des=request.POST['textarea']
        amount=request.POST['textfield4']
        rob=room()
        ob=cottage.objects.get(id=cott_num)
        rob.cottage_id=ob
        rob.room_number=room_num
        rob.room_facility=r_facility
        rob.number_of_persons=nofper
        rob.description=des
        rob.photo=fs
        rob.rate=amount
        rob.status='available'
        rob.save()
        return HttpResponse('''<script>alert("Successfully Added ");window.location="/manage_rooms"</script>''')
    except:
        return HttpResponse('''<script>alert("Enter a unique room number");window.location="/add_rooms"</script>''')

def add_fac(request):
    facility_name=request.POST['textfield']
    faci_des=request.POST['textarea']
    amount=request.POST['textfield2']

    fob=facilities()
    fob.faci_name=facility_name
    fob.desc=faci_des
    fob.rate=amount
    fob.save()
    return HttpResponse('''<script>alert("Successfully Added ");window.location="/manage_facilities"</script>''')

def add_eve(request):
    eventname = request.POST['textfield']
    des = request.POST['textarea']
    pic = request.FILES['file']
    fn = FileSystemStorage()
    fs = fn.save(pic.name, pic)
    amount = request.POST['textfield2']

    eob=events()
    eob.event_name=eventname
    eob.eve_desc=des
    eob.photo=fs
    eob.rate=amount
    eob.save()
    return HttpResponse('''<script>alert("Successfully Added ");window.location="/manage_events"</script>''')

def add_off(request):
    nofper=request.POST['textfield']
    amount=request.POST['textfield2']
    str_date=request.POST['textfield4']
    enddate=request.POST['textfield5']
    off_price=request.POST['textfield3']
    package1=request.POST['select']


    oob=offers()
    oob.number_of_persn=nofper
    oob.rate=amount
    oob.start_date=str_date
    oob.end_date=enddate
    oob.offer_price=off_price
    ob=package.objects.get(id=package1)
    oob.package_id=ob
    oob.save()
    return HttpResponse('''<script>alert("Successfully Added ");window.location="/manage_offers"</script>''')

def add_pack(request):
    package_name=request.POST['textfield']
    pic = request.FILES['file']
    fn = FileSystemStorage()
    fs = fn.save(pic.name, pic)
    amount=request.POST['textfield2']
    des=request.POST['textarea']
    stdate = request.POST['textfield3']
    endate = request.POST['textfield4']

    pob=package()
    pob.pack_name=package_name
    pob.rate=amount
    pob.photo=fs
    pob.description=des
    pob.start_date = stdate
    pob.end_date = endate
    pob.save()
    return HttpResponse('''<script>alert("Successfully Added ");window.location="/manage_package"</script>''')


def add_cott(request):
    try:
        cot_num = request.POST['textfield']
        cot_det = request.POST['textarea']
        num_room = request.POST['textfield2']
        cot_faci = request.POST['textarea2']
        cob = cottage()
        cob.cottage_num = cot_num
        cob.cottage_details = cot_det
        cob.number_rooms = num_room
        cob.cottage_facility = cot_faci
        cob.save()
        return HttpResponse('''<script>alert("Successfully Added ");window.location="view_cottage"</script>''')
    except Exception as e:
        print(e,"=======================")

        return HttpResponse('''<script>alert("enter a unique cottage number ");window.location="view_cottage"</script>''')


def update_emp(request):
    try:
        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        places=request.POST['textfield3']
        streets=request.POST['textfield4']
        pincod=request.POST['textfield5']
        cityy=request.POST['textfield6']
        districts=request.POST['select']
        states=request.POST['textfield7']
        mob=request.POST['textfield8']
        gendr=request.POST['radiobutton']
        adarnum=request.POST['textfield14']
        salaries=request.POST['textfield10']
        empltype=request.POST['select2']
        jobtitl=request.POST['textfield11']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)

        eob=employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname=fname
        eob.lastname=lname
        eob.place=places
        eob.street=streets
        eob.city=cityy
        eob.pincode=pincod
        eob.state=states
        eob.district=districts
        eob.phone=mob
        eob.gender=gendr
        eob.adarnumber=adarnum
        eob.salary=salaries
        eob.emptype=empltype
        eob.jobtitle=jobtitl
        eob.photo=fs
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="manage_employee"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        places = request.POST['textfield3']
        streets = request.POST['textfield4']
        pincod = request.POST['textfield5']
        cityy = request.POST['textfield6']
        districts = request.POST['select']
        states = request.POST['textfield7']
        mob = request.POST['textfield8']
        gendr = request.POST['radiobutton']
        adarnum = request.POST['textfield14']
        salaries = request.POST['textfield10']
        empltype = request.POST['select2']
        jobtitl = request.POST['textfield11']
        eob = employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname = fname
        eob.lastname = lname
        eob.place = places
        eob.street = streets
        eob.city = cityy
        eob.pincode = pincod
        eob.state = states
        eob.district = districts
        eob.phone = mob
        eob.gender = gendr
        eob.adarnumber = adarnum
        eob.salary = salaries
        eob.emptype = empltype
        eob.jobtitle = jobtitl
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="manage_employee"</script>''')

def update_cott(request):
    cot_num = request.POST['textfield']
    cot_det = request.POST['textarea']
    num_room = request.POST['textfield2']
    cot_faci = request.POST['textarea2']
    cob = cottage.objects.get(id=request.session['lid'])
    cob.cottage_num = cot_num
    cob.cottage_details = cot_det
    cob.number_rooms = num_room
    cob.cottage_facility = cot_faci
    cob.save()
    return HttpResponse('''<script>alert("Successfully updated ");window.location="view_cottage"</script>''')

def update_eve(request):
    try:
        eventname = request.POST['textfield']
        des = request.POST['textarea']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)
        amount = request.POST['textfield2']
        eob = events.objects.get(id=request.session['lid'])
        eob.event_name = eventname
        eob.eve_desc = des
        eob.photo = fs
        eob.rate = amount
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated ");window.location="/manage_events"</script>''')
    except:
        eventname = request.POST['textfield']
        des = request.POST['textarea']
        amount = request.POST['textfield2']
        eob = events.objects.get(id=request.session['lid'])
        eob.event_name = eventname
        eob.eve_desc = des
        eob.rate = amount
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated ");window.location="/manage_events"</script>''')

def update_faci(request):
    facility_name = request.POST['textfield']
    faci_des = request.POST['textarea']
    amount = request.POST['textfield2']

    fob = facilities.objects.get(id=request.session['lid'])
    fob.faci_name = facility_name
    fob.desc = faci_des
    fob.rate = amount
    fob.save()
    return HttpResponse('''<script>alert("Successfully updated ");window.location="/manage_facilities"</script>''')

def update_off(request):
    nofper = request.POST['textfield']
    amount = request.POST['textfield2']
    str_date = request.POST['textfield4']
    enddate = request.POST['textfield5']
    off_price = request.POST['textfield3']
    package1 = request.POST['select']

    oob = offers.objects.get(id=request.session['lid'])
    oob.number_of_persn = nofper
    oob.rate = amount
    oob.start_date = str_date
    oob.end_date = enddate
    oob.offer_price = off_price
    ob = package.objects.get(id=package1)
    oob.package_id = ob
    oob.save()
    return HttpResponse('''<script>alert("Successfully Updated ");window.location="/manage_offers"</script>''')

def updte_package(request):
    try:
        package_name = request.POST['textfield']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)
        amount = request.POST['textfield2']
        des = request.POST['textarea']

        pob = package.objects.get(id=request.session['lid'])
        pob.pack_name = package_name
        pob.photo=fs
        pob.rate = amount
        pob.description = des
        pob.save()
        return HttpResponse('''<script>alert("Successfully updated ");window.location="/manage_package"</script>''')
    except:
        package_name = request.POST['textfield']
        amount = request.POST['textfield2']
        des = request.POST['textarea']

        pob = package.objects.get(id=request.session['lid'])
        pob.pack_name = package_name
        pob.rate = amount
        pob.description = des
        pob.save()
        return HttpResponse('''<script>alert("Successfully updated ");window.location="/manage_package"</script>''')

def update_room(request):
    try:
        cott_num = request.POST['select1']
        room_num = request.POST['textfield2']
        nofper = request.POST['textfield3']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)
        r_facility = request.POST['select']
        des = request.POST['textarea']
        amount = request.POST['textfield4']
        rob = room.objects.get(id=request.session['lid'])
        ob = cottage.objects.get(id=cott_num)
        rob.cottage_id = ob
        rob.room_number = room_num
        rob.room_facility = r_facility
        rob.number_of_persons = nofper
        rob.photo = fs
        rob.description = des
        rob.rate = amount
        rob.save()
        return HttpResponse('''<script>alert("Successfully updated ");window.location="/manage_rooms"</script>''')
    except:
        cott_num = request.POST['select1']
        room_num = request.POST['textfield2']
        nofper = request.POST['textfield3']
        r_facility = request.POST['select']
        des = request.POST['textarea']
        amount = request.POST['textfield4']
        rob = room.objects.get(id=request.session['lid'])
        ob = cottage.objects.get(id=cott_num)
        rob.cottage_id = ob
        rob.room_number = room_num
        rob.room_facility = r_facility
        rob.number_of_persons = nofper
        rob.description = des
        rob.rate = amount
        rob.save()
        return HttpResponse('''<script>alert("Successfully updated ");window.location="/manage_rooms"</script>''')


# Users form designs

def user_reg(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    places=request.POST['textfield3']
    streets=request.POST['textfield4']
    cityy=request.POST['textfield5']
    zip_postal=request.POST['textfield6']
    state_prov_reg=request.POST['textfield7']
    country=request.POST['textfield8']
    gendr=request.POST['radiobutton']
    mobile=request.POST['textfield9']
    id_proof=request.FILES['file']
    fn = FileSystemStorage()
    fs = fn.save(id_proof.name, id_proof)
    emails=request.POST['textfield11']
    nationality=request.POST['radiobutton']
    usname=request.POST['textfield12']
    paswrd=request.POST['textfield13']


    lob=login()
    lob.username=usname
    lob.password=paswrd
    lob.type='user'
    lob.save()
    uob=registration()
    uob.firstname=fname
    uob.lastname=lname
    uob.place=places
    uob.street=streets
    uob.city=cityy
    uob.pincode=zip_postal
    uob.state=state_prov_reg
    uob.country=country
    uob.gender=gendr
    uob.phone=mobile
    uob.idproof=fs
    uob.email=emails
    uob.nationality=nationality
    uob.loginid=lob
    uob.save()
    return HttpResponse('''<script>alert("Successfully Registered");window.location="/"</script>''')


def user_home(request):
    return render(request,'us_home_page.html')
def book_facility(request):
    return render(request,'us_book facility.html')
def emp_chat(request):
    return render(request,'us_emp_chat.html')

def registration_user(request):
    return render(request,'us_registration form.html')
def view_facilities(request):
    ob = facilities.objects.all()
    return render(request,'us_view facility.html',{'val':ob})
def view_cottages(request):
    ob = cottage.objects.all()
    return render(request, 'us_view_cottage.html', {'val': ob})


##################################################

def view_book_details(request):
    # request.session['lid'] = id
    ob = booking.objects.filter(user_id__loginid__id=request.session['lid'])
    return render(request,'us_view_book_det.html',{'val':ob})

#######################################################



def view_offers(request):
    ob = offers.objects.all()
    return render(request,'us_view_offers.html',{'val':ob})
# Room Bookings
def view_rooms(request):
    ob=room.objects.filter(status='available')
    return render(request, 'us_view room.html', {'val':ob})
    # ll=[]
    # for i in range(0,len(ob)):
    #     ll.append(i)
    # print(ob)
    # print(ll)
    # res=[]
    # for i in ob:
    #     res.append(i)
def book_room(request,id):
    b=room.objects.get(id=id)
    request.session['rid']=id
    b1=registration.objects.get(loginid=request.session['lid'])
    print(b1,"==============mmmmmmm")
    ob = package.objects.all()
    ob1 = facilities.objects.all()
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate, "======")
    return render(request,'us_book room.html',{'val': ob, 'val1': ob1,'uob':b1,'cdt':cdate})
def add_booking_det(request):
    from datetime import datetime
    roomfac=request.POST['select']
    pack=request.POST['selectp']
    print(pack,"+++++++++++++++++++++++")
    extra_faci=request.POST['select']
    nofpersn=request.POST['textfield5']
    nofadults=request.POST['textfield6']
    nofchildren=request.POST['textfield7']
    date_arr=request.POST['textfield8']
    date_vacc=request.POST['textfield9']
    aob=booking()
    ob=room.objects.get(id=request.session['rid'])
    aob.room_fac=roomfac
    ob4 = package.objects.get(id=pack)
    prate=ob4.rate
    print(ob4.rate,"====================================")
    ob2 = facilities.objects.get(id=extra_faci)
    print(ob2.rate,"================")
    frate=ob2.rate
    ob3 = registration.objects.get(loginid=request.session['lid'])
    aob.number_of_persn = nofpersn
    aob.adults = nofadults
    aob.childrens = nofchildren
    aob.date_arrival = date_arr
    aob.date_vaccate = date_vacc
    aob.user_id = ob3
    aob.room_id=ob
    aob.facilities_id=ob2
    aob.package_id=ob4
    aob.booking_date=datetime.today()
    aob.status='pending'
    start_date1 = datetime.strptime(date_arr, "%Y-%m-%d").date()
    end_date1 = datetime.strptime(date_vacc, "%Y-%m-%d").date()
    diff = abs((end_date1 - start_date1).days)
    print(diff, "++++++++++++++")
    total = ob.rate * diff + prate + frate
    print(total, "=======")
    # pob=offers.objects.get(number_of_persn=nofpersn,)
    # print(pob,"=================================================================")
    ###########################################################
    # try:
    # ofr = offers.objects.filter(package_id=pack,start_date__gte=date_arr,end_date__lte=date_vacc)
    # for i in ofr:
    #     discount = total - i.offer_price
    #     print(total,i.offer_price)
    #     print(discount,"ddddddddddddddddddddddddddd")
    #     request.session['total']=discount
    #     aob.total_amount=discount
    #     aob.save()
    #     request.session['bid']=aob
    # return HttpResponse('''<script>alert("Your booking is done");window.location="/us_room_payment"</script>''')
    # except:
    # #########################################################
    request.session['total']=total
    aob.total_amount = total
    aob.save()
    ob.status='un-available'
    ob.save()
    return HttpResponse('''<script>alert("Your booking is done");window.location="/us_room_payment"</script>''')

def us_room_payment(request):
    tot=request.session['total']
    bob=booking.objects.all().aggregate(Max('id'))
    print(bob,"=============================")
    request.session['bid']=bob['id__max']
    return render(request, 'us_room_payment.html', {'tot': tot})

def us_rooms_payment(request):
    bankname = request.POST['select']
    ifc = request.POST['textfield']
    pinnum = request.POST['textfield2']
    accno = request.POST['textfield3']
    tot = request.session['total']
    try:
        ob = bank.objects.get(bank_name=bankname, ifsc=ifc, account_no=accno, pin=pinnum)
        print(ob, "=========================")
        ob.amount = ob.amount - tot
        ob.save()
        ob1 = booking.objects.get(id=request.session['bid'])
        print(ob1)
        ob1.status = 'paid'
        ob1.save()
        return HttpResponse('''<script>alert("Payment done");window.location="/view_rooms"</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid User");window.location="/view_rooms"</script>''')
 # Event Booking
def view_events(request):
    ob=events.objects.all()
    return render(request, 'us_view events.html',{'val':ob})
def book_events (request,id):
    b = events.objects.all()
    request.session['eid'] = id
    b1=registration.objects.get(loginid__id=request.session['lid'])
    from time import gmtime, strftime
    cdate = strftime("%Y-%m-%d", gmtime())
    print(cdate, "======")
    return render(request,'us_book events.html',{'val':b,'val1':b1,'cdt':cdate})
def add_event_booking(request):
    eventname = request.POST['select']
    date = request.POST['textfield4']
    require = request.POST['textarea']
    eob = event_book()
    ob = events.objects.get(id=request.session['eid'])
    ob1 = registration.objects.get(loginid__id=request.session['lid'])
    eob.user_id = ob1
    ob3 = events.objects.get(id=eventname)
    eob.event_id = ob3
    eob.booking_date = date
    eob.requirements = require
    eob.status='pending'
    total = ob.rate
    print(total, "=======")
    request.session['total'] = total
    eob.total_amount = total
    eob.save()

    return HttpResponse('''<script>alert("Your booking is done");window.location="/us_event_payment"</script>''')
def us_event_payment(request):
    tot = request.session['total']
    return render(request, 'us_event_payment.html',{'tot':tot})
def event_payment(request):
    bankname = request.POST['select']
    ifc = request.POST['textfield']
    pinnum = request.POST['textfield2']
    accno = request.POST['textfield3']
    tot = request.session['total']
    try:
        ob = bank.objects.get(bank_name=bankname, ifsc=ifc, account_no=accno, pin=pinnum)
        print(ob, "=========================")
        ob.amount = ob.amount - tot
        ob.save()
        obbb=event_book.objects.aggregate(Max('id'))
        ob1 = event_book.objects.get(id=obbb['id__max'])
        print(ob1)
        ob1.status = 'paid'
        ob1.save()
        return HttpResponse('''<script>alert("Payment done");window.location="/view_events"</script>''')
    except:
         return HttpResponse('''<script>alert("Invalid User");window.location="/view_events"</script>''')

 ########################################
 # packages

def view_packages(request):
    ob=package.objects.all()
    return render(request,'us_view packages.html',{'val':ob})

#sending feedback and rating

def send_feedback(request):
    return render(request, 'us_send_feedback_rating.html')

def add_feedback(request):
    feedbacks = request.POST['textarea']
    ratings = request.POST['select']
    fob = feedback()
    ob1 = registration.objects.get(loginid__id=request.session['lid'])
    fob.user_id = ob1
    fob.description=feedbacks
    fob.rating=ratings
    fob.date=datetime.today()
    fob.save()
    return HttpResponse('''<script>alert("feedback send");window.location="/send_feedback"</script>''')

def search_month_report(request):
    month = request.POST['select']
    ob=booking.objects.filter(booking_date__month=month).count()
    ob1 = event_book.objects.filter(booking_date__month=month).count()
    ob2 = package.objects.all().count()
    ob3 = facilities.objects.all().count()
    ob5 = employee.objects.all().count()
    ob6 = cottage.objects.all().count()
    ob7 = room.objects.all().count()
    ob8 = menu.objects.all().count()
    return render(request, 'Admin_resort_report_.html', {'val': ob,'val1': ob1,'val2': ob2,'val3': ob3,'val5': ob5,'val6': ob6,'val7':ob7,'val8':ob8})

def us_view_menu(request):
    ob=menu.objects.all()
    return render(request,'us_view_food.html',{'val':ob})
def us_continue_menu(request,id):
    ob=menu.objects.get(id=id)
    request.session['mid']=id
    return render(request,'us_order_food.html',{'val': ob})
def us_order_menu(request):
    btn=request.POST['Submit']
    qua = request.POST['textfield']
    if btn=="Order Now":
        v=menu_orders.objects.filter(status='pending',user_id__loginid__id=request.session['lid'])
        v1=menu_orders.objects.filter(status='paid',user_id__loginid__id=request.session['lid'])
        print(v,v1,"++++++++++++++++++++")
        if len(v) == 0 or len(v1)!= 0:
            print("firstblock======================")
            ob = menu_orders()
            us = registration.objects.get(loginid__id=request.session['lid'])
            ob.user_id = us
            ob.book_date = datetime.today()
            ob.total_amount = '0'
            ob.status = 'pending'
            ob.save()
            ####################################
            ob1 =menu_order_details()
            ob1.quantity=qua
            ob1.status='ordered'
            mob=menu.objects.get(id=request.session['mid'])
            mob.stock=int(mob.stock) -int(qua)
            mob.save()
            ob1.menu_id=mob
            ob1.menu_orderid=ob
            ob1.save()
            return  HttpResponse('''<script>alert("Order Successfully done");window.location="/us_purchased_food"</script>''')
        else:
            print("secondblock======================")
            v = menu_orders.objects.filter(status='pending', user_id__loginid__id=request.session['lid']).aggregate(
                Max('id'))
            print(v, "*********************")
            print("4444444444444================================")
            ob1 = menu_order_details()
            ob1.quantity = qua
            ob1.status = 'ordered'
            mob = menu.objects.get(id=request.session['mid'])
            ob1.menu_id = mob
            mob.stock=int(mob.stock) -int(qua)
            mob.save()
            oob=menu_orders.objects.get(id=v['id__max'])
            ob1.menu_orderid = oob
            ob1.save()
            return HttpResponse(
                '''<script>alert("Order Successfully done");window.location="/us_purchased_food"</script>''')
    else:
        v = menu_orders.objects.filter(status='pending', user_id__loginid__id=request.session['lid'])
        v1 = menu_orders.objects.filter(status='paid', user_id__loginid__id=request.session['lid'])
        print(v, v1, "++++++++++++++++++++")
        if len(v) == 0 or len(v1) != 0:
            print("firstblock======================")
            ob = menu_orders()
            us = registration.objects.get(loginid__id=request.session['lid'])
            ob.user_id = us
            ob.book_date = datetime.today()
            ob.total_amount = '0'
            ob.status = 'pending'
            ob.save()
            ####################################
            ob1 = menu_order_details()
            ob1.quantity = qua
            ob1.status = 'ordered'
            mob = menu.objects.get(id=request.session['mid'])
            mob.stock=int(mob.stock) -int(qua)
            mob.save()
            ob1.menu_id = mob
            ob1.menu_orderid = ob
            ob1.save()
            return redirect('/us_view_menu')
        else:
            print("secondblock======================")
            v = menu_orders.objects.filter(status='pending', user_id__loginid__id=request.session['lid']).aggregate(
                Max('id'))
            print(v, "*********************")
            print("4444444444444================================")
            ob1 = menu_order_details()
            ob1.quantity = qua
            ob1.status = 'ordered'
            mob = menu.objects.get(id=request.session['mid'])
            ob1.menu_id = mob
            mob.stock=int(mob.stock) -int(qua)
            mob.save()
            oob = menu_orders.objects.get(id=v['id__max'])
            ob1.menu_orderid = oob
            ob1.save()
            return redirect('/us_view_menu')
def us_purchased_food(request):
    ob = menu_order_details.objects.filter(menu_orderid__user_id__loginid__id=request.session['lid'],menu_orderid__status='pending')
    print(ob,"+++++++++++++++++++++")
    tot=0
    for i in ob:
        price=i.quantity * i.menu_id.rate
        tot=tot+price
    print(tot,"+++++++++++++")
    request.session['total']=tot
    return render(request, 'us_food_paymentss.html',{'val':ob,'tot':tot})

def user_payments(request):
    tot=request.session['total']
    return render(request,'us_payment.html',{'tot':tot})

def us_food_payment(request):
    bankname = request.POST['select']
    ifc = request.POST['textfield']
    pinnum = request.POST['textfield2']
    accno = request.POST['textfield3']
    tot = request.session['total']
    try:
        ob=bank.objects.get(bank_name=bankname,ifsc=ifc,account_no=accno,pin=pinnum)
        print(ob,"=========================")
        ob.amount = ob.amount - tot
        ob.save()
        obb = menu_order_details.objects.filter(menu_orderid__user_id__loginid__id=request.session['lid'],
                                                menu_orderid__status='pending').values('menu_orderid').distinct()
        print(obb, "=======")
        for i in obb:
            ob1 = menu_orders.objects.get(id=i['menu_orderid'])
            print(ob1)
            ob1.status = 'paid'
            ob1.total_amount=tot
            ob1.save()
        return HttpResponse('''<script>alert("Payment done");window.location="/us_view_menu"</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid User");window.location="/user_payments"</script>''')


#Employee functions
def emp_kitchen_home(request):
    return render(request,'emp_kitchen_home_page.html')
def emp_room_home(request):
    return render(request,'emp_room_home_page.html')

def emp_view_booking(request):
    ob=booking.objects.all()
    return render(request,'employee_view_book_det.html',{'val':ob})
def purchase_req(request):
    return render(request,'emp_send_purchase_reqst.html')
def send_purchase_req(request):
    matrlname = request.POST['textarea']
    qua = request.POST['textfield']
    pob=request_materials()
    ob1 = employee.objects.get(loginid__id=request.session['lid'])
    pob.emp_id = ob1
    pob.material_det=matrlname
    pob.quantity=qua
    pob.status='pending'
    pob.save()
    return HttpResponse('''<script>alert("New Material request send");window.location="/purchase_req"</script>''')

def emp_view_salary(request):
    ob = employee.objects.get(loginid__id=request.session['lid'])
    return render(request,'emp_view_salary.html',{'val':ob})

def send_leave(request):
    return render(request,'emp_send_leave_reqst.html')

def send_leave_request(request):
    reasons = request.POST['textarea']
    dates = request.POST['textfield']
    tdate = request.POST['textfield1']
    lob=leave()
    ob1 = employee.objects.get(loginid__id=request.session['lid'])
    lob.employeeid = ob1
    lob.reason = reasons
    lob.requestdate = dates
    lob.date = datetime.today()
    lob.todate = tdate
    lob.status='pending'
    lob.save()
    return HttpResponse('''<script>alert("Leave request send");window.location="/send_leave"</script>''')

def view_leave_status(request):
    ob = leave.objects.filter(employeeid__loginid__id=request.session['lid'])
    return render(request, 'emp_leave_status.html', {'val': ob})

def emp_food_menu(request):
    ob=menu.objects.all()
    return render(request, 'emp_manage_food.html',{'val':ob})

def add_food(request):
    ob=menu.objects.all()
    return render(request,'emp_add_food.html',{'val':ob})

def add_food1(request):
    item = request.POST['textfield2']
    item_des=request.POST['textarea']
    pic=request.FILES['file']
    amount=request.POST['textfield5']
    qua=request.POST['textfield4']
    fn=FileSystemStorage()
    fs=fn.save(pic.name,pic)
    fob=menu()
    fob.item_name=item
    fob.item_description=item_des
    fob.stock=qua
    fob.rate=amount
    fob.photo=fs
    fob.save()
    return HttpResponse('''<script>alert("Successfully Added ");window.location="/emp_food_menu"</script>''')

def editfood (request,id):
    request.session['mid'] = id
    ob = menu.objects.get(id=id)
    return render(request,'emp_edit_food.html',{'val':ob})

def deletefood(request,id):
    ob = menu.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/emp_food_menu"</script>''')

def update_food(request):
    item = request.POST['textfield2']
    item_des=request.POST['textarea']
    pic=request.FILES['file']
    amount=request.POST['textfield5']
    qua=request.POST['textfield4']
    fn=FileSystemStorage()
    fs=fn.save(pic.name,pic)
    fob=menu.objects.get(id=request.session['mid'])
    fob.item_name=item
    fob.item_description=item_des
    fob.stock=qua
    fob.rate=amount
    fob.photo=fs
    fob.save()
    return HttpResponse('''<script>alert("Successfully updated ");window.location="/emp_food_menu"</script>''')

def emp_view_attendance(request):
    return render(request, 'emp_view_attendance.html')

def emp_search_attendance(request):
    mnth = request.POST['select']
    btn = request.POST['Submit']
    if btn == "SEARCH":
        try:
            ob1 = attendance.objects.filter(date__month=mnth).values('date').distinct()
            print(ob1.count(), "*********")
            import calendar
            # now=datetime.now()
            mnth_day=int(mnth)
            mob=calendar.monthrange(2022,mnth_day)[1]
            ob = attendance.objects.filter(date__month=mnth,employee_id__loginid__id=request.session['lid']).values('employee_id').annotate(Sum('attendance'),
                                                                                            Avg('attendance'))
            print(ob, "=obbbbbbb==================")
            obb = attendance.objects.filter(date__month=mnth,employee_id__loginid__id=request.session['lid']).values('employee_id').annotate(total=Count('attendance'))
            print(obb, "obbbbbbbbbbbbbbbb")
            for i in obb:
                att = i['total'] / ob1.count() * 100
                print(att, "==============================")
            return render(request, 'emp_view_attendance.html', {'val': obb, 'v': mob,'cnt':ob1.count(), 'per': att,'mnth':int(mnth)})
        except:
            return render(request, 'emp_view_attendance.html', {'val': obb, 'v': 0, 'per': 0,'mnth':int(mnth)})
    else:
        return render(request, 'emp_view_attendance.html')

#Employee Rooms functions

def room_view_booking(request):
    ob = booking.objects.all()
    return render(request, 'emproom_usrooms_booking_report.html',{'val':ob})
################################################
def event_booking_users(request):
    ob = booking.objects.all()
    return render(request, 'emproom_event_bookings_userdet.html',{'val': ob})

def event_view_booking(request,id):
    ob = event_book.objects.filter(user_id__loginid__id=id)
    return render(request, 'emproom_event_bookings.html',{'val': ob})
##################################################
def room_send_leave(request):
    return render(request,'emp_room_send_leave_reqst.html')

def room_send_leave_request(request):
    reasons = request.POST['textarea']
    dates = request.POST['textfield']
    tdate = request.POST['textfield1']
    lob=leave()
    ob1 = employee.objects.get(loginid__id=request.session['lid'])
    lob.employeeid = ob1
    lob.reason = reasons
    lob.requestdate = dates
    lob.todate=tdate
    lob.date = datetime.today()
    lob.status='pending'
    lob.save()
    return HttpResponse('''<script>alert("Leave request send");window.location="/room_send_leave"</script>''')

def room_view_leave_status(request):
    ob = leave.objects.filter(employeeid__loginid__id=request.session['lid'])
    return render(request, 'emp_room_leave_status.html', {'val': ob})

def room_purchase_req(request):
    return render(request,'emp_room_send_purchase_reqst.html')
def room_send_purchase_req(request):
    matrlname = request.POST['textarea']
    qua = request.POST['textfield']
    pob=request_materials()
    ob1 = employee.objects.get(loginid__id=request.session['lid'])
    pob.emp_id = ob1
    pob.material_det=matrlname
    pob.quantity=qua
    pob.status='pending'
    pob.save()
    return HttpResponse('''<script>alert("New Material request send");window.location="/room_purchase_req"</script>''')

def emp_room_view_attendance(request):
    ob = attendance.objects.all()
    return render(request, 'emp_room_view_attendance.html', {'val': ob})
def emp_room_search_attendance(request):
    mnth = request.POST['select']
    btn = request.POST['Submit']
    if btn == "SEARCH":
        try:
            ob1 = attendance.objects.filter(date__month=mnth).values('date').distinct()
            print(ob1.count(), "*********")
            import calendar
            # now=datetime.now()
            mnth_day = int(mnth)
            mob = calendar.monthrange(2022, mnth_day)[1]
            ob = attendance.objects.filter(date__month=mnth, employee_id__loginid__id=request.session['lid']).values(
                'employee_id').annotate(Sum('attendance'),
                                        Avg('attendance'))
            print(ob, "=obbbbbbb==================")
            obb = attendance.objects.filter(date__month=mnth, employee_id__loginid__id=request.session['lid']).values(
                'employee_id').annotate(total=Count('attendance'))
            print(obb, "obbbbbbbbbbbbbbbb")
            for i in obb:
                att = i['total'] / ob1.count() * 100
                print(att, "==============================")
            return render(request, 'emp_room_view_attendance.html', {'val': obb, 'v': mob,'cnt':ob1.count(), 'per': att,'mnth':int(mnth)})
        except:
            return render(request, 'emp_room_view_attendance.html', {'val': obb, 'v': 0, 'per': 0,'mnth':int(mnth)})
    else:
        return render(request, 'emp_room_view_attendance.html')
#
def view_orderdet_users(request):
    ob=menu_orders.objects.all()
    return render(request, 'emp_view_user_food_details.html', {'val': ob})
def view_user_ordered_items(request):
    ob=menu_order_details.objects.all()
    return render(request, 'emp_view_user_items_orders.html', {'val': ob})

def emp_room_update_profile(request):
    # request.session['lid'] = id
    ob = employee.objects.get(loginid__id=request.session['lid'])
    return render(request, 'emproom_update_profile.html',{'val':ob})
def emp_update_prof(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        places = request.POST['textfield3']
        streets = request.POST['textfield4']
        pincod = request.POST['textfield5']
        cityy = request.POST['textfield6']
        districts = request.POST['select']
        states = request.POST['textfield7']
        mob = request.POST['textfield8']
        gendr = request.POST['radiobutton']
        adarnum = request.POST['textfield14']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)
        eob = employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname = fname
        eob.lastname = lname
        eob.place = places
        eob.street = streets
        eob.city = cityy
        eob.pincode = pincod
        eob.state = states
        eob.district = districts
        eob.phone = mob
        eob.gender = gendr
        eob.adarnumber = adarnum
        eob.photo = fs
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="emp_room_update_profile"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        places = request.POST['textfield3']
        streets = request.POST['textfield4']
        pincod = request.POST['textfield5']
        cityy = request.POST['textfield6']
        districts = request.POST['select']
        states = request.POST['textfield7']
        mob = request.POST['textfield8']
        gendr = request.POST['radiobutton']
        adarnum = request.POST['textfield14']
        eob = employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname = fname
        eob.lastname = lname
        eob.place = places
        eob.street = streets
        eob.city = cityy
        eob.pincode = pincod
        eob.state = states
        eob.district = districts
        eob.phone = mob
        eob.gender = gendr
        eob.adarnumber = adarnum
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="emp_room_update_profile"</script>''')

def emp_kitchen_update_profile(request):
    # request.session['lid'] = id
    ob = employee.objects.get(loginid__id=request.session['lid'])
    return render(request, 'empkitchen_update_profile.html',{'val':ob})
def emp_kitchen_update_prof(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        places = request.POST['textfield3']
        streets = request.POST['textfield4']
        pincod = request.POST['textfield5']
        cityy = request.POST['textfield6']
        districts = request.POST['select']
        states = request.POST['textfield7']
        mob = request.POST['textfield8']
        gendr = request.POST['radiobutton']
        adarnum = request.POST['textfield14']
        pic = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(pic.name, pic)
        eob = employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname = fname
        eob.lastname = lname
        eob.place = places
        eob.street = streets
        eob.city = cityy
        eob.pincode = pincod
        eob.state = states
        eob.district = districts
        eob.phone = mob
        eob.gender = gendr
        eob.adarnumber = adarnum
        eob.photo = fs
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="emp_kitchen_update_profile"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        places = request.POST['textfield3']
        streets = request.POST['textfield4']
        pincod = request.POST['textfield5']
        cityy = request.POST['textfield6']
        districts = request.POST['select']
        states = request.POST['textfield7']
        mob = request.POST['textfield8']
        gendr = request.POST['radiobutton']
        adarnum = request.POST['textfield14']
        eob = employee.objects.get(loginid__id=request.session['lid'])
        eob.firstname = fname
        eob.lastname = lname
        eob.place = places
        eob.street = streets
        eob.city = cityy
        eob.pincode = pincod
        eob.state = states
        eob.district = districts
        eob.phone = mob
        eob.gender = gendr
        eob.adarnumber = adarnum
        eob.save()
        return HttpResponse('''<script>alert("Successfully Updated");window.location="emp_kitchen_update_profile"</script>''')


