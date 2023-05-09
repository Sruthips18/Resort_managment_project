from django.db import models

# Create your models here.


class login(models.Model):
    username=models.CharField (max_length= 100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)


class registration(models.Model):
    loginid=models.ForeignKey(login,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone= models.BigIntegerField()
    idproof = models.FileField()
    email= models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)


class employee(models.Model):
    loginid = models.ForeignKey(login, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    phone= models.BigIntegerField()
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    adarnumber = models.BigIntegerField()
    salary = models.BigIntegerField()
    emptype = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=50)
    photo = models.FileField()


class leave(models.Model):
    employeeid = models.ForeignKey(employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)
    reason = models.TextField()
    requestdate = models.DateField()
    todate = models.DateField()


class cottage(models.Model):
    cottage_num = models.IntegerField()
    cottage_details = models.TextField()
    number_rooms = models.IntegerField()
    cottage_facility = models.CharField(max_length=50)


class room(models.Model):
    room_number = models.CharField(max_length=50)
    cottage_id = models.ForeignKey(cottage, on_delete=models.CASCADE)
    room_facility = models.CharField(max_length=50)
    number_of_persons = models.IntegerField()
    description = models.TextField()
    photo = models.FileField()
    rate = models.BigIntegerField()
    status=models.CharField(max_length=50)


class events(models.Model):
     event_name= models.CharField(max_length=50)
     eve_desc = models.TextField()
     rate = models.BigIntegerField()
     photo = models.FileField()


class feedback(models.Model):
    user_id = models.ForeignKey(registration, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField()
    date = models.DateField()



class menu(models.Model):
   item_name= models.CharField(max_length=50)
   item_description = models.TextField()
   rate = models. BigIntegerField()
   stock = models.BigIntegerField()
   photo = models.FileField()



class chat(models.Model):
    user_id = models.ForeignKey(login, on_delete=models.CASCADE,related_name='user_id')
    emp_id = models.ForeignKey(login, on_delete=models.CASCADE,related_name='emp_id')
    message = models.TextField()
    date_time = models.DateTimeField()


class package(models.Model):
    pack_name = models.CharField(max_length=50)
    rate = models.BigIntegerField()
    photo = models.FileField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class offers(models.Model):
    package_id = models.ForeignKey(package, on_delete=models.CASCADE)
    number_of_persn = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    offer_price = models.FloatField()


class facilities(models.Model):
    faci_name = models.CharField(max_length=50)
    rate= models.BigIntegerField()
    desc = models.TextField()


class booking(models.Model):
    user_id = models.ForeignKey(registration, on_delete=models.CASCADE)
    room_id = models.ForeignKey(room, on_delete=models.CASCADE)
    facilities_id = models.ForeignKey(facilities, on_delete=models.CASCADE)
    package_id = models.ForeignKey(package, on_delete=models.CASCADE)
    number_of_persn = models.IntegerField()
    adults = models.IntegerField()
    childrens = models.IntegerField()
    date_arrival = models.DateField()
    date_vaccate = models.DateField()
    status = models.CharField(max_length=50)
    booking_date = models.DateField()
    total_amount=models.FloatField()
class menu_orders(models.Model):
    user_id = models.ForeignKey(registration, on_delete=models.CASCADE)
    book_date = models.DateField()
    total_amount = models.BigIntegerField()
    status = models.CharField(max_length=30)

class menu_order_details(models.Model):
    menu_orderid=models.ForeignKey(menu_orders, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(menu, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    status = models.CharField(max_length=30)


class event_book(models.Model):
    event_id = models.ForeignKey(events, on_delete=models.CASCADE)
    user_id = models.ForeignKey(registration, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    requirements = models.TextField(max_length=100)
    booking_date = models.DateField()


class request_materials(models.Model):
    material_det = models.CharField(max_length=100)
    emp_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    status = models.CharField(max_length=50)


class salary_info(models.Model):
    emp_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    salary_amount = models.BigIntegerField()
    date = models.DateTimeField()
    status = models.CharField(max_length=50)


class bank(models.Model):
    bank_name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    pin = models.BigIntegerField()
    account_no = models.BigIntegerField()
    amount = models.FloatField()



class attendance(models.Model):
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    date = models.DateField()
    attendance = models.IntegerField()








