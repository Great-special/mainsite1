from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from .forms import DeliveryBookingForms
from .models import Booking_delivery

# Create your views here.


def home(request):
    # return render(request, "jumbotron.html")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def delivery(request):

    if request.method == 'POST':
        forms = DeliveryBookingForms(request.POST)
        if forms.is_valid():
            senderFullname = forms.cleaned_data['senderFullname']
            senderContactAddress = forms.cleaned_data['senderContactAddress']
            senderPhoneno = forms.cleaned_data['senderPhoneNo']

            receiverFullname = forms.cleaned_data['receiverFullname']
            receiverContactAddress = forms.cleaned_data['receiverContactAddress']
            receiverPhoneNo = forms.cleaned_data['receiverPhoneNo']

            package_name = forms.cleaned_data['package_name']
            package_details = forms.cleaned_data['package_details']

            location_from = forms.cleaned_data['location_from']
            location_to = forms.cleaned_data['location_to']

            urgent = forms.cleaned_data['urgent']
            tracking_code = get_random_string(16)

            booking_form = Booking_delivery(
                sender_name=senderFullname,
                sender_address=senderContactAddress,
                sender_phone_no=senderPhoneno,

                receiver_name=receiverFullname,
                receiver_address=receiverContactAddress,
                receiver_phone_no=receiverPhoneNo,

                package_name=package_name,
                package_desc=package_details,
                location_sender=location_from,
                location_receiver=location_to,
                urgent=urgent,
                tracking_code=tracking_code,

            )
            booking_form.save()
            return render(request, "form_feedback.html", {

                'sender_name': senderFullname,
                'sender_address': senderContactAddress,
                'sender_phone_no': senderPhoneno,

                'receiver_name': receiverFullname,
                'receiver_address': receiverContactAddress,
                'receiver_phone_no': receiverPhoneNo,

                'package_name': package_name,
                'package_details': package_details,
                'location_from': location_from,
                'location_to': location_to,

                'tracking_code':   tracking_code,
            })
    else:
        forms = DeliveryBookingForms()
        return render(request, "booking_form.html", {'forms': forms})

