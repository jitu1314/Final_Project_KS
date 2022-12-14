from django.contrib import admin
from django.urls import path, include
from client import client_views

urlpatterns = [
    path('home/', client_views.home),
    path('clogin/', client_views.clogin),
    path('registration/', client_views.registration),
    path('pregistration/', client_views.pregistration),
    path('contactus/', client_views.contact),
    path('forgotpass/', client_views.forgotpass),
    path('sendotp/', client_views.sendemail),
    path('reset/', client_views.set_password),
    path('services/', client_views.services),
    path('services/<int:id>', client_views.services),
    path('gallery/', client_views.gallerytable),
    path('gallery3/', client_views.gallery3),
    path('blog/', client_views.blog),
    path('planpricing/', client_views.planpricing),
    path('planpricing/<int:id>', client_views.planpricing),
    path('updateprofile/', client_views.updateprofile),
    path('editprofile/<int:id>', client_views.editprofile),
    path('bookingpackage/<int:id>/<int:amt>', client_views.packagebooking),
    path('viewbooking/', client_views.bookingview),
    path('viewcategory/<int:id>', client_views.categorydetail),
    path('photosgallery/', client_views.photosgallery),
    path('feedback/<int:pid>', client_views.feedbackinsert),
    path('clientbooking/<int:pid>/<int:amt>', client_views.clientbooking),
    path('cash/<int:id>', client_views.cash),
    path('clogout/', client_views.clientlogout),
    path('failure/', client_views.failure),
    path('success/<int:id>', client_views.success),
    path('psuccess/<int:id>', client_views.photosuccess),
    path('userprofile/', client_views.userprofile),
    path('viewfeedback/<int:id>', client_views.viewfeedback),
    path('updatebooking/<int:id>', client_views.bookingupdate),
    path('editbooking/<int:pid>/<int:amt>/<int:id>', client_views.bookingedit),
    path('pkgupdatebooking/<int:id>', client_views.bookingupdatepkg),
    path('pkgeditbooking/<int:pkid>/<int:amt>/<int:id>', client_views.bookingeditpkg),
    path('search/', client_views.search),
    path('cancelbooking/<int:id>', client_views.cancelbooking),
    path('addfilter/', client_views.filtergallery),
    path('appfilter/<int:id>', client_views.grayscale),
    path('appfilters/', client_views.fillgrayscale),
]