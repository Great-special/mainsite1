from django import forms


class OrderingForms(forms.Form):
    Fullname = forms.CharField(label='Name', max_length=150)
    Address = forms.CharField(label='Address', max_length=200)
    PhoneNo = forms.CharField(label='Phone No', max_length=11)

    # dish_name = forms.CharField(label='Dish')
