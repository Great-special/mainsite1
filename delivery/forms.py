
from django import forms


class DeliveryBookingForms(forms.Form):
    senderFullname = forms.CharField(label='Senders Name', max_length=150)
    senderContactAddress = forms.CharField(label='Senders Address', max_length=200)
    senderPhoneNo = forms.CharField(label='Senders Phone No', max_length=11)

    receiverFullname = forms.CharField(label='Receiver Name', max_length=150)
    receiverContactAddress = forms.CharField(label='Receiver Address', max_length=200)
    receiverPhoneNo = forms.CharField(label='Receiver Phone No', max_length=11)

    package_name = forms.CharField(label='Package Name')
    package_details = forms.CharField(label='Package Details', widget=forms.Textarea)

    location_from = forms.CharField(label='Location From')
    location_to = forms.CharField(label='Location TO')

    urgent = forms.BooleanField(label='Urgent')
    # timing = forms.ChoiceField(choices=[('urgent', 'Urgent'), ('not urgent', 'Not Urgent')])


