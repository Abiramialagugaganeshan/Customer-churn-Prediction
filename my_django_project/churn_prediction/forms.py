from django import forms

class ChurnPredictionForm(forms.Form):
    # Define your form fields here
    months = forms.IntegerField(label='Months')
    uniqsubs = forms.IntegerField(label='Unique Subscribers')
    actvsubs = forms.IntegerField(label='Active Subscribers')
    totcalls = forms.IntegerField(label='Total Calls')
    totmou = forms.FloatField(label='Total Minutes of Use')
    totrev = forms.FloatField(label='Total Revenue')
    avgrev = forms.FloatField(label='Average Revenue')
    avgmou = forms.FloatField(label='Average Minutes of Use')
    avgqty = forms.FloatField(label='Average Quantity')
    eqpdays = forms.IntegerField(label='Equipment Days')
    total_truck = forms.IntegerField(label='Total Truck')
