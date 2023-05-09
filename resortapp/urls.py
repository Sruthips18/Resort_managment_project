from django.urls import path

from resortapp import views

urlpatterns = [
    path('',views.login1,name='login1'),
    path('loginbtn',views.loginbtn,name='loginbtn'),
    path('Admin_home_page', views.Admin_home_page, name='Admin_home_page'),
    path('add_employees', views.add_employees, name='add_employees'),
    path('add_events', views.add_events, name='add_events'),
    path('add_facilities',views.add_facilities,name='add_facilities'),
    path('add_offers',views.add_offers,name='add_offers'),
    path('add_packages',views. add_packages,name=' add_packages'),
    path('add_rooms',views.add_rooms,name='add_rooms'),
    path('approve_reject_leave',views.approve_reject_leave,name='approve_reject_leave'),
    path('manage_booking_info',views.manage_booking_info,name='manage_booking_info'),
    path('manage_employee',views.manage_employee,name='manage_employee'),
    path('manage_events',views.manage_events,name='manage_events'),
    path('manage_facilities',views.manage_facilities,name='manage_facilities'),
    path('manage_offers', views.manage_offers, name='manage_offers'),
    path('manage_package', views.manage_package, name='manage_package'),
    path('manage_purchase_det', views.manage_purchase_det, name='manage_purchase_det'),
    path('manage_rooms', views.manage_rooms, name='manage_rooms'),
    path('reason_leave', views.reason_leave, name='reason_leave'),
    path('view_feedback_rating', views.view_feedback_rating, name='view_feedback_rating'),
    path('view_users', views.view_users, name='view_users'),
    path('view_reports_resort', views.view_reports_resort, name='view_reports_resort'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('users_booking_report', views.users_booking_report, name='users_booking_report'),
    path('employee_salary', views.employee_salary, name='employee_salary'),
    path('view_cottage', views.view_cottage, name='view_cottage'),
    path('add_cottage', views.add_cottage, name='add_cottage'),
    path('manage_event_booking',views.manage_event_booking, name='manage_event_booking'),
    path('search_attendance',views.search_attendance,name='search_attendance'),

    path('search_month_report',views.search_month_report,name='search_month_report'),

    path('add_emp', views.add_emp, name='add_emp'),
    path('add_room', views.add_room, name='add_room'),
    path('add_fac', views.add_fac, name='add_fac'),
    path('add_eve', views.add_eve, name='add_eve'),
    path('add_off', views.add_off, name='add_off'),
    path('add_pack', views.add_pack, name='add_pack'),
    path('add_cott', views.add_cott, name='add_cott'),
    path('addbutton',views.addbutton, name='addbutton'),
    path('search',views.search,name='search'),
    path('admbooking',views.admbooking,name='admbooking'),
    path('fdpaymnt',views.fdpaymnt,name='fdpaymnt'),

    path('manage_purchase_det_status',views.manage_purchase_det_status,name='manage_purchase_det_status'),
    #Delection proces

    path('deleteemp/<int:id>',views.deleteemp,name='deleteemp'),
    path('deleteeve/<int:id>',views.deleteeve,name='deleteeve'),
    path('deletefac/<int:id>',views.deletefac,name='deletefac'),
    path('deleteoff/<int:id>',views.deleteoff,name='deleteoff'),
    path('deletepack/<int:id>',views.deletepack,name='deletepack'),
    path('deleteroom/<int:id>',views.deleteroom,name='deleteroom'),
    path('deletecott/<int:id>',views.deletecott,name='deletecott'),

 # editing

    path('editemployee/<int:id>',views.editemployee, name='editemployee'),
    path('editevent/<int:id>',views.editevent, name='editevent'),
    path('editfacility/<int:id>',views.editfacility, name='editfacility'),
    path('editoffers/<int:id>',views.editoffers, name='editoffers'),
    path('editpack/<int:id>',views.editpack, name='editpack'),
    path('editroom/<int:id>',views.editroom, name='editroom'),
    path('editcottage/<int:id>',views.editcottage, name='editcottage'),

# updation

    path('update_emp', views.update_emp, name='update_emp'),
    path('update_cott',views.update_cott, name='update_cott'),
    path('update_eve',views.update_eve, name='update_eve'),
    path('update_faci',views.update_faci, name='update_faci'),
    path('update_off',views.update_off, name='update_off'),
    path('updte_package',views.updte_package, name='updte_package'),
    path('update_room',views.update_room, name='update_room'),

# Approve and reject

    path('approve_book_det/<int:id>',views.approve_book_det, name='approve_book_det'),
    path('reject_purchase_det/<int:id>',views.reject_purchase_det, name='reject_purchase_det'),
    path('reject_book_det/<int:id>',views.reject_book_det, name='reject_book_det'),
    path('approve_purchase_det/<int:id>', views.approve_purchase_det, name='approve_purchase_det'),
    path('approve_leave_req/<int:id>',views.approve_leave_req, name='approve_leave_req'),
    path('reject_leave_req/<int:id>', views.reject_leave_req, name='reject_leave_req'),

    path('approve_eve_book/<int:id>',views.approve_eve_book, name='approve_eve_book'),
    path('reject_eve_book/<int:id>',views.reject_eve_book, name='reject_eve_book'),


    # Users forms

    path('user_home',views.user_home, name='user_home'),
    path('book_events/<int:id>', views.book_events, name='book_events'),
    path('book_facility', views.book_facility, name='book_facility'),
    path('book_room/<int:id>', views.book_room, name='book_room'),
    path('emp_chat', views.emp_chat, name='emp_chat'),
    path('user_payments', views.user_payments, name='user_payments'),
    path('registration_user', views.registration_user, name='registration_user'),
    path('view_events', views.view_events, name='view_events'),
    path('view_facilities', views.view_facilities, name='view_facilities'),
    path('view_packages', views.view_packages, name='view_packages'),
    path('view_rooms', views.view_rooms, name='view_rooms'),

    path('view_book_details', views.view_book_details, name='view_book_details'),

    path('view_offers', views.view_offers, name='view_offers'),
    path('user_reg',views.user_reg, name='user_reg'),
    path('add_feedback',views.add_feedback,name='add_feedback'),
    path('view_cottages',views.view_cottages,name='view_cottages'),
    path('send_feedback',views.send_feedback,name='send_feedback'),
    path('add_attendance',views.add_attendance,name='add_attendance'),
    path('us_view_menu',views.us_view_menu,name='us_view_menu'),
    path('us_continue_menu/<int:id>',views.us_continue_menu,name='us_continue_menu'),
    path('us_order_menu',views.us_order_menu,name='us_order_menu'),
    path('us_food_payment',views.us_food_payment,name='us_food_payment'),
    path('us_purchased_food',views.us_purchased_food,name='us_purchased_food'),
    path('us_room_payment',views.us_room_payment,name='us_room_payment'),
    path('us_rooms_payment',views.us_rooms_payment,name='us_rooms_payment'),
    path('admin_update_room_status',views.admin_update_room_status,name='admin_update_room_status'),
    path('search_room_status',views.search_room_status,name='search_room_status'),
    path('available_status/<int:id>',views.available_status,name='available_status'),

# bookings

    path('add_booking_det',views.add_booking_det, name='add_booking_det'),
    path('add_event_booking',views.add_event_booking,name='add_event_booking'),
    path('us_event_payment',views.us_event_payment,name='us_event_payment'),
    path('event_payment',views.event_payment,name='event_payment'),

# Employees

    path('emp_kitchen_home', views.emp_kitchen_home, name='emp_kitchen_home'),
    path('emp_room_home', views.emp_room_home, name='emp_room_home'),
    path('emp_view_booking',views.emp_view_booking,name='emp_view_booking'),
    path('purchase_req',views.purchase_req,name='purchase_req'),
    path('emp_view_salary',views.emp_view_salary,name='emp_view_salary'),
    path('send_leave',views.send_leave,name='send_leave'),
    path('send_leave_request',views.send_leave_request,name='send_leave_request'),
    path('view_leave_status',views.view_leave_status,name='view_leave_status'),
    path('emp_food_menu',views.emp_food_menu,name='emp_food_menu'),
    path('add_food',views.add_food,name='add_food'),
    path('add_food1',views.add_food1,name='add_food1'),
    path('update_food',views.update_food,name='update_food'),
    path('editfood/<int:id>', views.editfood, name='editfood'),
    path('deletefood/<int:id>', views.deletefood, name='deletefood'),
    path('emp_view_attendance',views.emp_view_attendance,name='emp_view_attendance'),
    path('send_purchase_req',views.send_purchase_req,name='send_purchase_req'),
    path('emp_search_attendance',views.emp_search_attendance,name='emp_search_attendance'),

    #room employee

    path('room_view_booking',views.room_view_booking,name='room_view_booking'),
    path('event_view_booking/<int:id>',views.event_view_booking,name='event_view_booking'),
    path('room_send_leave', views.room_send_leave, name='room_send_leave'),
    path('room_send_leave_request', views.room_send_leave_request, name='room_send_leave_request'),
    path('room_view_leave_status', views.room_view_leave_status, name='room_view_leave_status'),
    path('room_purchase_req', views.room_purchase_req, name='room_purchase_req'),
    path('room_send_purchase_req', views.room_send_purchase_req, name='room_send_purchase_req'),
    path('emp_room_search_attendance', views.emp_room_search_attendance, name='emp_room_search_attendance'),
    path('emp_room_view_attendance', views.emp_room_view_attendance, name='emp_room_view_attendance'),
    path('view_orderdet_users',views.view_orderdet_users,name='view_orderdet_users'),
    path('view_user_ordered_items',views.view_user_ordered_items,name='view_user_ordered_items'),
    path('emp_room_update_profile',views.emp_room_update_profile,name='emp_room_update_profile'),
    path('emp_update_prof',views.emp_update_prof,name='emp_update_prof'),
    path('emp_kitchen_update_profile',views.emp_kitchen_update_profile,name='emp_kitchen_update_profile'),
    path('emp_kitchen_update_prof', views.emp_kitchen_update_prof, name='emp_kitchen_update_prof'),
    path('event_booking_users',views.event_booking_users,name='event_booking_users'),

]

