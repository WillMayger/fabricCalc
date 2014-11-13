from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from fabric import models
from fabric import forms


def loopResourceVPViewsLoop():
    RES_CHOICES = []
    res_choice = models.Product.objects.get(pk=privateOrKick).resource.all()

    for resItem in res_choice:

        if models.Product.objects.get(pk=privateOrKick).resource.get(name='Additional App Resource Bundle') != resItem \
            and models.Product.objects.get(pk=privateOrKick).resource.get(name='Additional App Runtime Bundle') != resItem:
            RES_CHOICES.append((str(resItem)))


    return RES_CHOICES



def FirstStagePageView(request):
    if request.method == 'POST':
            licenceCheckBox = request.POST['licenceCheckBox']
            monthlyChoice = request.POST['monthlyradiobuttons']
            privateOrKick = request.POST['privateOrKick']

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()



            editionVcpu = edition.resource.get(name='Additional App Resource Bundle')
            editionRam = edition.resource.get(name='Additional App Runtime Bundle')
            editionStorage = ""

            editionVcpuPer = editionVcpu
            editionRamPer = editionRam
            editionStoragePer = editionStorage

            popUpList = []
            if privateOrKick == 1:
                resForm = forms.ResourceDropDownKS( auto_id = True )
            else:

                resForm = forms.ResourceDropDownVP( auto_id = True)
            numForm = forms.NumberInputFormVP( auto_id = True )

            for i in loopResourceVPViewsLoop():

                editionResourceDescription = edition.resource.get(name=i).description
                popUpList.append(i + ": ")
                popUpList.append(str(editionResourceDescription))
                popUpList.append("   ")
            addResourceName = str(editionVcpu)
            addRuntimeName = str(editionRam)

            resourceDes = editionVcpu.description
            runtimeDes = editionRam.description

            template = loader.get_template('fabric/kickstartedition.html')
            context = RequestContext(request, {'editionName': editionName,
                                       'editionResource':editionResource,
                                       'resourceDes': resourceDes,
                                       'runtimeDes': runtimeDes,
                                       'addResourceName': addResourceName,
                                       'addRuntimeName': addRuntimeName,
                                       'popUpList':popUpList,
                                       'numForm': numForm,
                                       'licenceCheckBox': licenceCheckBox,
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

            licenceCheckBox = request.POST['licenceCheckBox']
            monthlyChoice = request.POST['monthlyChoice']
            privateOrKick = int(request.POST['privateOrKick'])

            resourceChoice = request.POST['Resources']

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()


            editionVcpu = edition.resource.get(name='Additional App Resource Bundle')
            editionRam = edition.resource.get(name='Additional App Runtime Bundle')
            editionStorage = ""

            editionVcpuPer = editionVcpu
            editionRamPer = editionRam
            editionStoragePer = editionStorage

            editionMonthlyCost = models.CostPerMonth.objects.\
                 filter(resource__product__pk=privateOrKick).\
                 filter(resource__name=str(resourceChoice)).\
                 get(lengthInMonths=int(monthlyChoice)).\
                 costPerMonth

            editionResourceDescription = edition.resource.get(name=str(resourceChoice)).description


            numForm = forms.NumberInputFormVP( auto_id = True )
            resForm = forms.ResourceDropDownVP( auto_id = True)
            popUpList = []
            for i in loopResourceVPViewsLoop():
                editionResourceDescription = edition.resource.get(name=str(i)).description
                popUpList.append(i + ": ")
                popUpList.append(str(editionResourceDescription))
                popUpList.append("   ")

            addResourceName = str(editionVcpu)
            addRuntimeName = str(editionRam)

            resourceDes = editionVcpu.description
            runtimeDes = editionRam.description

            template = loader.get_template('fabric/kseresource.html')
            context = RequestContext(request, {'editionName': editionName,
                                           'editionResource': editionResource,
                                           'licenceCheckBox': licenceCheckBox,
                                           'addResourceName': addResourceName,
                                           'addRuntimeName': addRuntimeName,
                                           'numForm': numForm,
                                           'popUpList': popUpList,
                                           'resourceDes': resourceDes,
                                           'runtimeDes': runtimeDes,
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
                                           'editionResourceDescription': editionResourceDescription
                                           })
            return HttpResponse(template.render(context))
    else:
        errorMessage = 'Please choose a Resource first!'

        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage})
        return HttpResponse(template.render(context))

def NumbersPageView(request):
    if request.method == 'POST':

            licenceCheckBox = request.POST['licenceCheckBox']

            privateOrKick = int(request.POST['privateOrKick'])

            edition = models.Product.objects.get(pk=privateOrKick)
            editionName = edition.name
            editionResource = edition.resource.all()

            monthlyChoice = request.POST['monthlyChoice']

            resourceChoice = request.POST['resourceChoice']
            editionMonthlyCost = float(request.POST['editionMonthlyCost'])



            editionVcpu = edition.resource.get(name='Additional App Resource Bundle')
            editionRam = edition.resource.get(name='Additional App Runtime Bundle')
            editionStorage = ""

            editionVcpuPer = editionVcpu
            editionRamPer = editionRam
            editionStoragePer = editionStorage

            try:
                vCPU = int(request.POST['resourceAD'])
            except:
                vCPU = 0

            editionVcpuCost = models.CostPerMonth.objects.\
                     filter(resource__product__pk=privateOrKick).\
                     filter(resource__name=editionVcpu).\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

            userVcpu = int(editionVcpuCost * int(vCPU))

            editionVcpu = str(editionVcpu) + " * " + str(vCPU)
            preUserRun = 0
            try:
                ram = int(request.POST['runtimeAD'])
                if resourceChoice != "Foundation +":
                    preUserRun = ram
                    ram = 0
            except:
                ram = 0


            editionRamCost = models.CostPerMonth.objects.\
                     filter(resource__product__pk=privateOrKick).\
                     filter(resource__name=editionRam).\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

            userRam = int(editionRamCost * int(ram))

            editionRam = str(editionRam) + " * " + str(ram)


            userStorage = 0

            totalCost = userStorage + userRam + userVcpu + editionMonthlyCost



            numForm = forms.NumberInputFormVP( auto_id = True )
            resForm = forms.ResourceDropDownVP( auto_id = True)

            addResourceName = str(editionVcpuPer)
            addRuntimeName = str(editionRamPer)

            popUpList = []
            for i in loopResourceVPViewsLoop():
                editionResourceDescription = edition.resource.get(name=str(i)).description
                popUpList.append(i + ": ")
                popUpList.append(str(editionResourceDescription))
                popUpList.append("   ")

            resourceDes = editionVcpuPer.description
            runtimeDes = editionRamPer.description




            template = loader.get_template('fabric/ksenumbers.html')
            context = RequestContext(request, {'editionName': editionName,
                                               'editionResource': editionResource,
                                               'numForm': numForm,
                                               'preUserRun': preUserRun,
                                               'popUpList': popUpList,
                                               'addResourceName': addResourceName,
                                               'addRuntimeName': addRuntimeName,
                                               'resourceDes': resourceDes,
                                               'runtimeDes': runtimeDes,
                                               'editionVcpu': editionVcpu,
                                               'editionRam': editionRam,
                                               'editionStorage': editionStorage,
                                               'editionVcpuPer': editionVcpuPer,
                                               'editionRamPer': editionRamPer,
                                               'licenceCheckBox': licenceCheckBox,
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
    global privateOrKick;
    privateOrKick = 1;
    try:
        if request.POST['licenceCheckBox'] == 'on':
            licenceCheckBox = True
            privateOrKick = 2
        else:
            licenceCheckBox = False
            privateOrKick = 1
    except:
        licenceCheckBox = False
        privateOrKick = 1

    monthForm = forms.MonthlyRadioButtons( auto_id = True )


    template = loader.get_template('fabric/monthlyvp.html')
    context = RequestContext(request, {'monthForm': monthForm, 'privateOrKick': privateOrKick, 'licenceCheckBox': licenceCheckBox})
    return HttpResponse(template.render(context))

def MonthlyKickStartPageView(request):
    monthForm = forms.MonthlyRadioButtons( auto_id = True )
    privateOrKick = 1
    template = loader.get_template('fabric/monthlykickstart.html')
    context = RequestContext(request, {'monthForm': monthForm, 'privateOrKick': privateOrKick})
    return HttpResponse(template.render(context))

def FrontPageView(request):


    privateEdition = models.Product.objects.get(pk=2)
    privateEditionName = privateEdition.name
    privateEditionDescription = privateEdition.description

    template = loader.get_template('fabric/frontpage.html')
    context = RequestContext(request, {'privateEditionName': privateEditionName,
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
