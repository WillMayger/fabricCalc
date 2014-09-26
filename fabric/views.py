#VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW----VIEW---
from decimal import Decimal
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from fabric import models
from fabric import forms


################################ KICK START EDITION FUNCTION ###########################################################
################################ KICK START EDITION FUNCTION ###########################################################
def KickStarterPageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputForm( auto_id = True )
    resForm = forms.ResourceDropDownKS( auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#-----------------getting monthly choice-------------------------------------------------------------------------------
            monthlyChoice = request.POST['monthlyradiobuttons']

#-----------------getting info on the product--------------------------------------------------------------------------
            KickStarterEdition = models.Product.objects.get(pk=1)
            EditionName = KickStarterEdition.name
            KickStarterEditionResource = KickStarterEdition.resource.all()

            KickStarterEditionvcpu = KickStarterEdition.resource.get(name='vCPU')
            KickStarterEditionRAM = KickStarterEdition.resource.get(name='Ram')
            KickStarterEditionSTORAGE = KickStarterEdition.resource.get(name='Storage')

#-------------------------------Getting all values and loading web page-------------------------------------------------
            template = loader.get_template('fabric/kickstartedition.html')
            context = RequestContext(request, {'EditionName': EditionName,
                                           'KickStarterEditionResource': KickStarterEditionResource,
                                           'numForm': numForm,
                                           'KickStarterEditionvcpu': KickStarterEditionvcpu,
                                           'KickStarterEditionRAM': KickStarterEditionRAM,
                                           'KickStarterEditionSTORAGE': KickStarterEditionSTORAGE,
                                           'monthlyChoice': monthlyChoice,
                                           'resForm': resForm})
            return HttpResponse(template.render(context))

#--------if anything that isnt a post method happens, run this next block of code---------------------------------------
    else:

#-----------------getting info on the product--------------------------------------------------------------------------
        errorMessage = 'Please choose a Monthly Term first!'

        KickStarterEdition = models.Product.objects.get(pk=1)
        EditionName = KickStarterEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################






################################ KICK START EDITION RESOURCE FUNCTION ##################################################
################################ KICK START EDITION RESOURCE FUNCTION ##################################################
def KSResourcePageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputForm( auto_id = True )
    resForm = forms.ResourceDropDownKS( auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#-----------------getting monthly choice-------------------------------------------------------------------------------
            monthlyChoice = request.POST['monthlyChoice']

#-----------------getting resource drop down choice-------------------------------------------------------------------------------
            resourceChoice = request.POST['Resources']

#-----------------getting info on the product--------------------------------------------------------------------------
            KickStarterEdition = models.Product.objects.get(pk=1)
            EditionName = KickStarterEdition.name
            KickStarterEditionResource = KickStarterEdition.resource.all()

            KickStarterEditionvcpu = KickStarterEdition.resource.get(name='vCPU')
            KickStarterEditionRAM = KickStarterEdition.resource.get(name='Ram')
            KickStarterEditionSTORAGE = KickStarterEdition.resource.get(name='Storage')

            KickStarterEditionMonthlyCost = models.CostPerMonth.objects.\
                 filter(resource__product__name=EditionName).\
                 filter(resource__name=str(resourceChoice)).\
                 get(lengthInMonths=int(monthlyChoice)).\
                 costPerMonth

#-------------------------------Getting all values and loading web page-------------------------------------------------
            template = loader.get_template('fabric/kseresource.html')
            context = RequestContext(request, {'EditionName': EditionName,
                                           'KickStarterEditionResource': KickStarterEditionResource,
                                           'numForm': numForm,
                                           'KickStarterEditionvcpu': KickStarterEditionvcpu,
                                           'KickStarterEditionRAM': KickStarterEditionRAM,
                                           'KickStarterEditionSTORAGE': KickStarterEditionSTORAGE,
                                           'monthlyChoice': monthlyChoice,
                                           'resForm': resForm,
                                           'resourceChoice': resourceChoice,
                                           'KickStarterEditionMonthlyCost': KickStarterEditionMonthlyCost})
            return HttpResponse(template.render(context))

#--------if anything that isnt a post method happens, run this next block of code---------------------------------------
    else:
        errorMessage = 'Please choose a Resource first!'

        KickStarterEdition = models.Product.objects.get(pk=1)
        EditionName = KickStarterEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################








################################ KICK START EDITION NUMBERS FUNCTION ####################################################
################################ KICK START EDITION NUMBERS FUNCTION ####################################################
def KSNumbersPageView(request):


#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputForm( auto_id = True )
    resForm = forms.ResourceDropDownKS( auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#-----------------getting info on the product--------------------------------------------------------------------------
            KickStarterEdition = models.Product.objects.get(pk=1)
            EditionName = KickStarterEdition.name
            KickStarterEditionResource = KickStarterEdition.resource.all()

#--------------------------------PREVIOUS CHOICE'S------------------------------------------------------------------------
            monthlyChoice = request.POST['monthlyChoice']

            resourceChoice = request.POST['resourceChoice']
            KickStarterEditionMonthlyCost = int(request.POST['KickStarterEditionMonthlyCost'])


#--------------------------------VCPU----------------------------------------------------------------------------------
            vCPU = request.POST['vcpu']

                     #--------NAME-----------#
            KickStarterEditionvcpu = KickStarterEdition.resource.filter(name='vCPU')[0]

                     #------------------#
            KickStarterEditionvcpuCost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name='vCPU').\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

                     #--------FINAL VARIABLE-----------#
            userVCPU = int(KickStarterEditionvcpuCost * int(vCPU))

#--------------------------------RAM----------------------------------------------------------------------------------
            Ram = request.POST['ram']

                     #--------NAME-----------#
            KickStarterEditionRAM = KickStarterEdition.resource.filter(name='Ram')[0]

                     #------------------#
            KickStarterEditionRAMCost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name='Ram').\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

                     #--------FINAL VARIABLE-----------#
            userRAM = int(KickStarterEditionRAMCost * int(Ram))

#--------------------------------STORAGE----------------------------------------------------------------------------------
            Storage = request.POST['storage']

                     #--------NAME-----------#
            KickStarterEditionSTORAGE = KickStarterEdition.resource.filter(name='Storage')[0]

                     #------------------#
            KickStarterEditionSTORAGECost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name='Storage').\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

                     #--------FINAL VARIABLE-----------#
            userSTORAGE = Decimal(KickStarterEditionSTORAGECost * int(Storage))

#---------------------------------------TOTAL COST--------------------------------------------------------------------
            totalCost = userSTORAGE + userRAM + userVCPU + KickStarterEditionMonthlyCost

#-------------------------------Getting all values and loading web page-------------------------------------------------
            template = loader.get_template('fabric/ksenumbers.html')
            context = RequestContext(request, {'EditionName': EditionName,
                                               'KickStarterEditionResource': KickStarterEditionResource,
                                               'numForm': numForm,
                                               'KickStarterEditionvcpu': KickStarterEditionvcpu,
                                               'KickStarterEditionRAM': KickStarterEditionRAM,
                                               'KickStarterEditionSTORAGE': KickStarterEditionSTORAGE,
                                               'monthlyChoice': monthlyChoice,
                                               'resForm': resForm,
                                               'userVCPU': userVCPU,
                                               'userRAM': userRAM,
                                               'userSTORAGE': userSTORAGE,
                                               'KickStarterEditionMonthlyCost': KickStarterEditionMonthlyCost,
                                               'resourceChoice': resourceChoice,
                                               'totalCost': totalCost,})
            return HttpResponse(template.render(context))

#--------if anything that isn't a post method happens, run this next block of code---------------------------------------
    else:

#-----------------getting info on the product--------------------------------------------------------------------------
        errorMessage = 'Please choose a Resource first!'

        KickStarterEdition = models.Product.objects.get(pk=1)
        EditionName = KickStarterEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################







################################ VIRTUAL PRIVATE EDITION FUNCTION ##################################################
################################ VIRTUAL PRIVATE EDITION FUNCTION ##################################################
def VirtualPrivatePageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputFormVP( auto_id = True )
    resForm = forms.ResourceDropDownVP( auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#-----------------getting monthly choice-------------------------------------------------------------------------------
            monthlyChoice = request.POST['monthlyradiobuttons']

#-----------------getting info on the product--------------------------------------------------------------------------
            PrivateEdition = models.Product.objects.get(pk=2)
            EditionName = PrivateEdition.name
            PrivateEditionResource = PrivateEdition.resource.all()

            PrivateEditionVCPU = PrivateEdition.resource.filter(name='Additional App resource bundle')[0]
            PrivateEditionRAM = PrivateEdition.resource.filter(name='Additional App runtime bundle')[0]

#-------------------------------Getting all values and loading web page-------------------------------------------------
            template = loader.get_template('fabric/virtualprivateedition.html')
            context = RequestContext(request, {'EditionName': EditionName,
                                           'PrivateEditionResource': PrivateEditionResource,
                                           'numForm': numForm,
                                           'PrivateEditionVCPU': PrivateEditionVCPU,
                                           'PrivateEditionRAM': PrivateEditionRAM,
                                           'monthlyChoice': monthlyChoice,
                                           'resForm': resForm})
            return HttpResponse(template.render(context))

#--------if anything that isnt a post method happens, run this next block of code---------------------------------------
    else:

#-----------------getting info on the product--------------------------------------------------------------------------
        errorMessage = 'Please choose a Monthly Term first!'

        PrivateEdition = models.Product.objects.get(pk=2)
        EditionName = PrivateEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################







################################ VIRTUAL PRIVATE EDITION RESOURCE FUNCTION ############################################
################################ VIRTUAL PRIVATE EDITION RESOURCE FUNCTION ############################################
def VPResourcePageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputFormVP( auto_id = True )
    resForm = forms.ResourceDropDownVP(auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#--------------------------------MONTHLY CHOICE------------------------------------------------------------------------
                monthlyChoice = request.POST['monthlyChoice']

#-----------------getting resource drop down choice-------------------------------------------------------------------------------
                resourceChoice = request.POST['Resources']

#-----------------getting info on the product--------------------------------------------------------------------------
                PrivateEdition = models.Product.objects.get(pk=2)
                EditionName = PrivateEdition.name
                PrivateEditionResource = PrivateEdition.resource.all()

                PrivateEditionVCPU = PrivateEdition.resource.filter(name='Additional App resource bundle')[0]
                PrivateEditionRAM = PrivateEdition.resource.filter(name='Additional App runtime bundle')[0]

                PrivateEditionMonthlyCost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name=str(resourceChoice)).\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth
#-------------------------------Getting all values and loading web page-------------------------------------------------
                template = loader.get_template('fabric/vperesource.html')
                context = RequestContext(request, {'EditionName': EditionName,
                                               'PrivateEditionResource': PrivateEditionResource,
                                               'numForm': numForm,
                                               'PrivateEditionVCPU': PrivateEditionVCPU,
                                               'PrivateEditionRAM': PrivateEditionRAM,
                                               'monthlyChoice': monthlyChoice,
                                               'resForm': resForm,
                                               'resourceChoice': resourceChoice,
                                               'PrivateEditionMonthlyCost': PrivateEditionMonthlyCost})
                return HttpResponse(template.render(context))

#--------if anything that isnt a post method happens, run this next block of code---------------------------------------
    else:

#-----------------getting info on the product--------------------------------------------------------------------------

#-----------------getting info on the product--------------------------------------------------------------------------
        errorMessage = 'Please choose a Resource first!'

        PrivateEdition = models.Product.objects.get(pk=2)
        EditionName = PrivateEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################







################################ VIRTUAL PRIVATE EDITION NUMBERS FUNCTION ##############################################
################################ VIRTUAL PRIVATE EDITION NUMBERS FUNCTION ##############################################
def VPNumbersPageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    numForm = forms.NumberInputFormVP( auto_id = True )
    resForm = forms.ResourceDropDownVP( auto_id = True)

#---------------if a POST method form has been started-----------------------------------------------------------------
    if request.method == 'POST':

#-----------------getting info on the product--------------------------------------------------------------------------
            PrivateEdition = models.Product.objects.get(pk=2)
            EditionName = PrivateEdition.name
            PrivateEditionResource = PrivateEdition.resource.all()

#--------------------------------PREVIOUS CHOICE'S------------------------------------------------------------------------
            monthlyChoice = request.POST['monthlyChoice']

            resourceChoice = request.POST['resourceChoice']
            PrivateEditionMonthlyCost = int(request.POST['PrivateEditionMonthlyCost'])

#--------------------------------resourceAD----------------------------------------------------------------------------------
            resourceAD = request.POST['resourceAD']

                     #--------NAME-----------#
            PrivateEditionVCPU = PrivateEdition.resource.filter(name='Additional App resource bundle')[0]

                     #------------------#
            PrivateEditionVCPUCost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name='Additional App resource bundle').\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

                     #--------FINAL VARIABLE-----------#
            userVCPU = int(PrivateEditionVCPUCost * int(resourceAD))

#--------------------------------RAM----------------------------------------------------------------------------------
            runtimeAD = request.POST['runtimeAD']

                     #--------NAME-----------#
            PrivateEditionRAM = PrivateEdition.resource.filter(name='Additional App runtime bundle')[0]

                     #------------------#
            PrivateEditionRAMCost = models.CostPerMonth.objects.\
                     filter(resource__product__name=EditionName).\
                     filter(resource__name='Additional App runtime bundle').\
                     get(lengthInMonths=int(monthlyChoice)).\
                     costPerMonth

                     #--------FINAL VARIABLE-----------#
            userRAM = int(PrivateEditionRAMCost * int(runtimeAD))

#---------------------------------------TOTAL COST--------------------------------------------------------------------
            totalCost =  userRAM + userVCPU + PrivateEditionMonthlyCost

#-------------------------------Getting all values and loading web page-------------------------------------------------
            template = loader.get_template('fabric/vpenumbers.html')
            context = RequestContext(request, {'EditionName': EditionName,
                                               'PrivateEditionResource': PrivateEditionResource,
                                               'numForm': numForm,
                                               'PrivateEditionVCPU': PrivateEditionVCPU,
                                               'PrivateEditionRAM': PrivateEditionRAM,
                                               'monthlyChoice': monthlyChoice,
                                               'resForm': resForm,
                                               'userVCPU': userVCPU,
                                               'userRAM': userRAM,
                                               'PrivateEditionMonthlyCost': PrivateEditionMonthlyCost,
                                               'resourceChoice': resourceChoice,
                                               'totalCost': totalCost})
            return HttpResponse(template.render(context))

#--------if anything that isnt a post method happens, run this next block of code---------------------------------------
    else:

#-----------------getting info on the product--------------------------------------------------------------------------
        PrivateEdition = models.Product.objects.get(pk=2)
        PrivateEditionName = PrivateEdition.name
        PrivateEditionResource = PrivateEdition.resource.all()

        PrivateEditionVCPU = PrivateEdition.resource.filter(name='vCPU')[0]
        PrivateEditionRAM = PrivateEdition.resource.filter(name='Ram')[0]
        PrivateEditionSTORAGE = PrivateEdition.resource.filter(name='Storage')[0]

#-------------------------------Getting all values and loading web page-------------------------------------------------

#-----------------getting info on the product--------------------------------------------------------------------------
        errorMessage = 'Please choose a Resource first!'

        PrivateEdition = models.Product.objects.get(pk=2)
        EditionName = PrivateEdition.name

#-------------------------------Getting all values and loading web page-------------------------------------------------
        template = loader.get_template('fabric/errorpage.html')
        context = RequestContext(request, {'errorMessage': errorMessage,
                                           'EditionName': EditionName})
        return HttpResponse(template.render(context))
########################################################################################################################








################################ VIRTUAL PRIVATE MONTHLY CHOICE ########################################################
################################ VIRTUAL PRIVATE MONTHLY CHOICE ########################################################
def MonthlyvpPageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    monthForm = forms.MonthlyRadioButtons( auto_id = True )

#-------------------------------Getting all values and loading web page-------------------------------------------------
    template = loader.get_template('fabric/monthlyvp.html')
    context = RequestContext(request, {'monthForm': monthForm})
    return HttpResponse(template.render(context))
########################################################################################################################








################################ KICK START EDITION MONTHLY CHOICE #####################################################
################################ KICK START EDITION MONTHLY CHOICE #####################################################
def MonthlyKickStartPageView(request):

#-----------------getting forms----------------------------------------------------------------------------------------
    monthForm = forms.MonthlyRadioButtons( auto_id = True )

#-------------------------------Getting all values and loading web page-------------------------------------------------
    template = loader.get_template('fabric/monthlykickstart.html')
    context = RequestContext(request, {'monthForm': monthForm})
    return HttpResponse(template.render(context))
########################################################################################################################








################################ FRONT PAGE FUNCTION ###################################################################
################################ FRONT PAGE FUNCTION ###################################################################
def FrontPageView(request):

#-----------------getting info on the product(KICK START)---------------------------------------------------------------
    KickStarterEdition = models.Product.objects.get(pk=1)
    KickStarterEditionName = KickStarterEdition.name
    KickStarterEditionDescription = KickStarterEdition.description

#-----------------getting info on the product(VIRTUAL PRIVATE)----------------------------------------------------------
    PrivateEdition = models.Product.objects.get(pk=2)
    PrivateEditionName = PrivateEdition.name
    PrivateEditionDescription = PrivateEdition.description

#-------------------------------Getting all values and loading web page-------------------------------------------------
    template = loader.get_template('fabric/frontpage.html')
    context = RequestContext(request, {'KickStarterEditionName': KickStarterEditionName,
                                       'KickStarterEditionDescription': KickStarterEditionDescription,
                                       'PrivateEditionName': PrivateEditionName,
                                       'PrivateEditionDescription': PrivateEditionDescription})
    return HttpResponse(template.render(context))
########################################################################################################################







############################# ERROR PAGE VIEW ##########################################################################
############################# ERROR PAGE VIEW ##########################################################################
def ErrorPageView(request):

    template = loader.get_template('fabric/errorpage.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
########################################################################################################################






################### 404 ################################################################################################
################### 404 ################################################################################################
def handlerCustom404(request):

     return render(request, 'fabric/404.html')
########################################################################################################################




################### 500 ################################################################################################
################### 500 ################################################################################################
def handlerCustom500(request):

     return render(request, 'fabric/500.html')
#######################################################################################################################