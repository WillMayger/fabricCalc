from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from fabric import models
from fabric import forms

def FirstStagePageView(request):
    if request.method == 'POST':
            monthlyChoice = request.POST['monthlyradiobuttons']
            privateOrKick = request.POST['privateOrKick']

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()

            if int(privateOrKick) == 1:
                editionVcpu = edition.resource.get(name='vCPU')
                editionRam = edition.resource.get(name='Ram')
                editionStorage = edition.resource.get(name='Storage')

                editionVcpuPer = str(editionVcpu) + "  (Per item)"
                editionRamPer = str(editionRam) + " (Per GB)"
                editionStoragePer = str(editionStorage) + " (Per GB)"

            if int(privateOrKick) == 2:
                editionVcpu = edition.resource.get(name='Additional App resource bundle')
                editionRam = edition.resource.get(name='Additional App runtime bundle')
                editionStorage = ""

                editionVcpuPer = editionVcpu
                editionRamPer = editionRam
                editionStoragePer = editionStorage

            if int(privateOrKick) == 1:
                numForm = forms.NumberInputForm( auto_id = True )
                resForm = forms.ResourceDropDownKS( auto_id = True)
            else:
                numForm = forms.NumberInputFormVP( auto_id = True )
                resForm = forms.ResourceDropDownVP( auto_id = True)

            template = loader.get_template('fabric/kickstartedition.html')
            context = RequestContext(request, {'editionName': editionName,
                                       'editionResource':editionResource,
                                       'numForm': numForm,
                                       'editionVcpu': editionVcpu,
                                       'editionRam': editionRam,
                                       'editionStorage': editionStorage,
                                       'editionVcpuPer': editionVcpuPer,
                                       'editionRamPer': editionRamPer,
                                       'editionStoragePer': editionStoragePer,
                                       'monthlyChoice': monthlyChoice,
                                       'resForm': resForm,
                                       'privateOrKick': privateOrKick,
                                       })
            return HttpResponse(template.render(context))
    else:

        errorMessage = 'Please choose a Monthly Term first!'

        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage})
        return HttpResponse(template.render(context))

def ResourcePageView(request):
    if request.method == 'POST':
            monthlyChoice = request.POST['monthlyChoice']
            privateOrKick = int(request.POST['privateOrKick'])

            resourceChoice = request.POST['Resources']

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()

            if int(privateOrKick) == 1:
                editionVcpu = edition.resource.get(name='vCPU')
                editionRam = edition.resource.get(name='Ram')
                editionStorage = edition.resource.get(name='Storage')

                editionVcpuPer = str(editionVcpu) + "  (Per item)"
                editionRamPer = str(editionRam) + " (Per GB)"
                editionStoragePer = str(editionStorage) + " (Per GB)"

            if int(privateOrKick) == 2:
                editionVcpu = edition.resource.get(name='Additional App resource bundle')
                editionRam = edition.resource.get(name='Additional App runtime bundle')
                editionStorage = ""

                editionVcpuPer = editionVcpu
                editionRamPer = editionRam
                editionStoragePer = editionStorage

            editionMonthlyCost = models.CostPerMonth.objects.\
                 filter(resource__product__name=editionName).\
                 filter(resource__name=str(resourceChoice)).\
                 get(lengthInMonths=int(monthlyChoice)).\
                 costPerMonth


            if int(privateOrKick) == 1:
                numForm = forms.NumberInputForm( auto_id = True )
                resForm = forms.ResourceDropDownKS( auto_id = True)
            else:
                numForm = forms.NumberInputFormVP( auto_id = True )
                resForm = forms.ResourceDropDownVP( auto_id = True)

            template = loader.get_template('fabric/kseresource.html')
            context = RequestContext(request, {'editionName': editionName,
                                           'editionResource': editionResource,
                                           'numForm': numForm,
                                           'editionVcpu': editionVcpu,
                                           'editionRam': editionRam,
                                           'editionStorage': editionStorage,
                                           'editionVcpuPer': editionVcpuPer,
                                           'editionRamPer': editionRamPer,
                                           'editionStoragePer': editionStoragePer,
                                           'monthlyChoice': monthlyChoice,
                                           'resForm': resForm,
                                           'resourceChoice': resourceChoice,
                                           'editionMonthlyCost': editionMonthlyCost,
                                           'privateOrKick': privateOrKick,
                                           })
            return HttpResponse(template.render(context))
    else:
        errorMessage = 'Please choose a Resource first!'

        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage})
        return HttpResponse(template.render(context))

def NumbersPageView(request):
    if request.method == 'POST':

            privateOrKick = int(request.POST['privateOrKick'])

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()

            monthlyChoice = request.POST['monthlyChoice']

            resourceChoice = request.POST['resourceChoice']
            editionMonthlyCost = float(request.POST['editionMonthlyCost'])

            if int(privateOrKick) == 1:
                editionVcpu = str(edition.resource.filter(name='vCPU')[0])
                editionRam = str(edition.resource.filter(name='Ram')[0])
                editionStorage = str(edition.resource.filter(name='Storage')[0])

                editionVcpuPer = str(editionVcpu) + "  (Per item)"
                editionRamPer = str(editionRam) + " (Per GB)"
                editionStoragePer = str(editionStorage) + " (Per GB)"

                vCPU = request.POST['vcpu']

                editionVcpuCost = models.CostPerMonth.objects.\
                         filter(resource__product__name=editionName).\
                         filter(resource__name='vCPU').\
                         get(lengthInMonths=int(monthlyChoice)).\
                         costPerMonth

                userVcpu = int(editionVcpuCost * int(vCPU))

                editionVcpu = editionVcpu + " * " + str(vCPU)

                ram = request.POST['ram']

                editionRamCost = models.CostPerMonth.objects.\
                         filter(resource__product__name=editionName).\
                         filter(resource__name='Ram').\
                         get(lengthInMonths=int(monthlyChoice)).\
                         costPerMonth

                userRam = int(editionRamCost * int(ram))

                editionRam = editionRam + " * " + str(ram)

                storage = request.POST['storage']

                editionStorageCost = models.CostPerMonth.objects.\
                         filter(resource__product__name=editionName).\
                         filter(resource__name='Storage').\
                         get(lengthInMonths=int(monthlyChoice)).\
                         costPerMonth

                userStorage = float(editionStorageCost * int(storage))

                editionStorage = editionStorage + " * " + str(storage)

                totalCost = userStorage + userRam + userVcpu + editionMonthlyCost

            else:

                editionVcpu = edition.resource.filter(name='Additional App resource bundle')[0]
                editionRam = edition.resource.filter(name='Additional App runtime bundle')[0]
                editionStorage = ""

                editionVcpuPer = editionVcpu
                editionRamPer = editionRam
                editionStoragePer = editionStorage

                vCPU = request.POST['resourceAD']

                editionVcpuCost = models.CostPerMonth.objects.\
                         filter(resource__product__name=editionName).\
                         filter(resource__name='vCPU').\
                         get(lengthInMonths=int(monthlyChoice)).\
                         costPerMonth

                userVcpu = int(editionVcpuCost * int(vCPU))

                editionVcpu = str(editionVcpu) + " * " + str(vCPU)

                ram = request.POST['runtimeAD']

                editionRamCost = models.CostPerMonth.objects.\
                         filter(resource__product__name=editionName).\
                         filter(resource__name='Ram').\
                         get(lengthInMonths=int(monthlyChoice)).\
                         costPerMonth

                userRam = int(editionRamCost * int(ram))

                editionRam = str(editionRam) + " * " + str(ram)


                userStorage = 0

                totalCost = userStorage + userRam + userVcpu + editionMonthlyCost


            if int(privateOrKick) == 1:
                numForm = forms.NumberInputForm( auto_id = True )
                resForm = forms.ResourceDropDownKS( auto_id = True)
            else:
                numForm = forms.NumberInputFormVP( auto_id = True )
                resForm = forms.ResourceDropDownVP( auto_id = True)

            template = loader.get_template('fabric/ksenumbers.html')
            context = RequestContext(request, {'editionName': editionName,
                                               'editionResource': editionResource,
                                               'numForm': numForm,
                                               'editionVcpu': editionVcpu,
                                               'editionRam': editionRam,
                                               'editionStorage': editionStorage,
                                               'editionVcpuPer': editionVcpuPer,
                                               'editionRamPer': editionRamPer,
                                               'editionStoragePer': editionStoragePer,
                                               'monthlyChoice': monthlyChoice,
                                               'resForm': resForm,
                                               'userVcpu': userVcpu,
                                               'userRam': userRam,
                                               'userStorage': userStorage,
                                               'editionMonthlyCost': editionMonthlyCost,
                                               'resourceChoice': resourceChoice,
                                               'totalCost': totalCost,
                                               'privateOrKick': privateOrKick,
                                               })
            return HttpResponse(template.render(context))
    else:

        errorMessage = 'Please choose a Resource first!'

        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage})
        return HttpResponse(template.render(context))

def MonthlyvpPageView(request):
    monthForm = forms.MonthlyRadioButtons( auto_id = True )
    privateOrKick = 2

    template = loader.get_template('fabric/monthlyvp.html')
    context = RequestContext(request, {'monthForm': monthForm, 'privateOrKick': privateOrKick})
    return HttpResponse(template.render(context))

def MonthlyKickStartPageView(request):
    monthForm = forms.MonthlyRadioButtons( auto_id = True )
    privateOrKick = 1
    template = loader.get_template('fabric/monthlykickstart.html')
    context = RequestContext(request, {'monthForm': monthForm, 'privateOrKick': privateOrKick})
    return HttpResponse(template.render(context))

def FrontPageView(request):
    kickStarterEdition = models.Product.objects.get(pk=1)
    kickStarterEditionName = kickStarterEdition.name
    kickStarterEditionDescription = kickStarterEdition.description

    privateEdition = models.Product.objects.get(pk=2)
    privateEditionName = privateEdition.name
    privateEditionDescription = privateEdition.description

    template = loader.get_template('fabric/frontpage.html')
    context = RequestContext(request, {'kickStarterEditionName': kickStarterEditionName,
                                       'kickStarterEditionDescription': kickStarterEditionDescription,
                                       'privateEditionName': privateEditionName,
                                       'privateEditionDescription': privateEditionDescription})
    return HttpResponse(template.render(context))

def ErrorPageView(request):

    template = loader.get_template('fabric/errorpage.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def handlerCustom404(request):
     return render(request, 'fabric/404.html')


def handlerCustom500(request):
     return render(request, 'fabric/500.html')
