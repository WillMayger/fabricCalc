from django import forms
from django.forms import widgets
from fabric import models


def loopResource():
    RES_CHOICES = []
    res_choice =  models.Product.objects.get(pk=1).resource.all()

    for i in res_choice:
        if str(i) == 'vCPU':
            hi = 'hi'

        elif str(i) == 'Ram':
            hi = 'hi'

        elif str(i) == 'Storage':
            hi = 'hi'

        else:
            RES_CHOICES.append((str(i.name), str(i)))

    return RES_CHOICES

def loopResourceVP():
    RES_CHOICES = []
    res_choice =  models.Product.objects.get(pk=2).resource.all()

    for i in res_choice:
        if str(i) == 'vCPU':
             hi = 'hi'

        elif str(i) == 'Ram':
             hi = 'hi'

        elif str(i) == 'Storage':
            hi = 'hi'

        elif str(i) == 'Additional App resource bundle':
             hi = 'hi'

        elif str(i) == 'Additional App runtime bundle':
            hi = 'hi'

        else:
            RES_CHOICES.append((str(i.name), str(i)))

    return RES_CHOICES

def loopMonths():
    CHOICES= []

    KickStarterEditionMonthly = models.CostPerMonth.objects.filter(resource_id =1)
    monthAmounts = range(0,len(KickStarterEditionMonthly))

    for i in monthAmounts:
        KickStarterEditionMonthlyI = KickStarterEditionMonthly[i].lengthInMonths

        CHOICES.append((str(KickStarterEditionMonthlyI), ''),)

    return CHOICES

class NumberInputForm(forms.Form):
    vcpu = forms.IntegerField(widget=forms.NumberInput, label='', min_value=0, initial=0)
    ram = forms.IntegerField(widget=forms.NumberInput, label='', min_value=0, initial=0)
    storage = forms.IntegerField(widget=forms.NumberInput, label='', min_value=0, initial=0)

class MonthlyRadioButtons(forms.Form):
    CHOICES= loopMonths()
    monthlyradiobuttons = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label='')


class ResourceDropDownKS(forms.Form):
    RES_CHOICES = loopResource()
    Resources = forms.ChoiceField(choices=RES_CHOICES, label='')

class ResourceDropDownVP(forms.Form):
    RES_CHOICES = loopResourceVP()
    Resources = forms.ChoiceField(choices=RES_CHOICES, label='')

class NumberInputFormVP(forms.Form):
    resourceAD = forms.IntegerField(widget=forms.NumberInput, label='', min_value=0, initial=0)
    runtimeAD = forms.IntegerField(widget=forms.NumberInput, label='', min_value=0, initial=0)


