from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from fabric import models
from fabric import forms

def loopResourceVPViewsLoop():
    RES_CHOICES = []
    res_choice = models.Product.objects.get(pk=ThePk).resource.all()
    for resItem in res_choice:
            RES_CHOICES.append((str(resItem)))

    return RES_CHOICES

def ErrorPageView(request):

    template = loader.get_template('fabric/errorpage.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def InputObjectList(editionAdResource):
    numForm = []
    i = 0
    for object in editionAdResource:
        numForm.append("numForm" + str(i))

        month_n_cost = models.CostPerMonth.objects.filter(resource__name=object.name)

        costList = []
        for obj in month_n_cost:
                costList.append({'months': obj.lengthInMonths, 'cost':obj.costPerMonth})

        numForm[i] = forms.InputBoxes( object.name.replace(" ", ""), object.name, 0, costList, object.description)
        i = i + 1
    return numForm

def DropDownList(editionResource):
    dropForm = []
    i = 0
    for object in editionResource:
        dropForm.append("dropForm" + str(i))

        month_n_cost = models.CostPerMonth.objects.filter(resource__name=object.name)
        id = object.id
        costList = []
        for obj in month_n_cost:
                costList.append({'months': obj.lengthInMonths, 'cost':obj.costPerMonth})

        dropForm[i] = forms.DropDownBoxes( object.name.replace(" ", ""), object.name, 0, costList, id)
        i = i + 1
    return dropForm

def MonthlyRads(editionResource):
    dropForm = []
    i = 0
    for object in editionResource:
        if object.name == "Foundation":


            month_n_cost = models.CostPerMonth.objects.filter(resource__name=object.name)

            for obj in month_n_cost:
                dropForm.append("dropForm" + str(i))

                strMonth = str(obj.lengthInMonths) + " Months Commitment"

                if int(obj.lengthInMonths) == 0:
                   strMonth = "Pay As You Go"

                dropForm[i] = forms.MonthlyRads( object.name.replace(" ", ""),
                                                 strMonth,
                                                 obj.lengthInMonths)
                i = i + 1
    return dropForm

def AddResourceCost(additionalRes, monthlyChoice, resName):
    additionalResCost = models.AdditionalCostPerMonth.objects. \
        filter(additionalResource__product__pk=ThePk). \
        filter(additionalResource__name=resName).all(). \
        get(lengthInMonths=monthlyChoice). \
        costPerMonth
    returnValue = int(additionalRes) * int(additionalResCost)
    return returnValue

def ResourceCost(monthlyChoice, resName):
     resCost = models.CostPerMonth.objects. \
        filter(resource__product__pk=ThePk). \
        filter(resource__name=resName). \
        get(lengthInMonths=monthlyChoice). \
        costPerMonth
     return resCost

def postAndSetVariable(monthlyChoice, request):
    resourceUser = request.POST['Resources']
    resName = str(resourceUser)
    mainResource = ResourceCost( monthlyChoice, resName)

    return resName, mainResource

def PopUpList(edition):
    popUpList = []
    for i in loopResourceVPViewsLoop():
        editionResourceDescription = edition.resource.get(name=str(i)).description
        popUpList.append(i + ": ")
        popUpList.append(str(editionResourceDescription))
        popUpList.append("   ")
    return popUpList

def MonthlyCosts(editionResource):
    dropForm = {}
    for resName in DropDownList(editionResource):
        resNameId = resName.id
        resName = resName.text
        resCost = models.CostPerMonth.objects.filter(resource_id=resNameId)
        dropForm[resName] = []

        for obj  in resCost:
            month = obj.lengthInMonths
            cost = obj.costPerMonth
            dropForm[resName].append({month:cost})
    return dropForm

def ParseInt(string):
    try:
        return int(string)
    except ValueError:
        print "'%s' Is not a valid int" % (string)
        return 0

def CreatingDictionaries(request):
    monthlyChoice = int(request.POST['monthRads'])
    requestDic = {}
    tableDic = {}
    for i in request.POST:
        if i.encode() != "csrfmiddlewaretoken" \
                and i.encode() != "Resources" \
                and i.encode() != "monthRads":

            value = ParseInt(request.POST[i].encode())
            if value < 0:
                    value = 0

            resName = i.encode()
            addResAndAmount = "%s * %s" % (resName, value)
            if value > 0:
                addCost = AddResourceCost(value, monthlyChoice, resName)
                tableDic[addResAndAmount] = [addCost, (addCost / value), i.encode(), value]
            else:
                addCost = 0
                value = 0
                tableDic[addResAndAmount] = [addCost, 0, i.encode(), value]
            requestDic[i.encode()] = [value, addCost]
    return monthlyChoice, requestDic, tableDic

def TotalCost(mainResource, resName, tableDic):
    totalCost = int(mainResource)
    for key, value in tableDic.items():
        if resName != "Foundation +" and value[2] == 'Additional App Runtime Bundle' and value[0] > 0:
            totalCost += 0
        else:
            totalCost += value[0]
    return totalCost

def CfCalcView(request):
    global ThePk
    ThePk = 1

    edition = models.Product.objects.get(pk=ThePk)
    editionName = edition.name
    editionResource = edition.resource.all()

    editionAdResource = edition.additionalResource.all()

    compare = MonthlyCosts(editionResource)

    additionalResources = edition.additionalResource.all()

    additionalInfoDic = {}
    for i in additionalResources:
        additionalInfoDic[i.name] = i.description

    popUpList = PopUpList(edition)
    dropDowns = DropDownList(editionResource)
    numForm = InputObjectList(editionAdResource)
    monthForm = MonthlyRads(editionResource)
    postTrue = False

    if request.method == 'POST':

        monthlyChoice, requestDic, tableDic = CreatingDictionaries(request)

        postTrue = True

        resName, mainResource = postAndSetVariable(monthlyChoice, request)

        totalCost = TotalCost(mainResource, resName, tableDic)

        template = loader.get_template('fabric/cfcalcpage.html')
        context = RequestContext(request, {
                                           'listOfNum': numForm,
                                           'dropDowns': dropDowns,
                                           'monthForm': monthForm,
                                           'compare': compare,
                                           'resName': resName,
                                           'mainResource': mainResource,
                                           'postTrue': postTrue,
                                           'totalCost': totalCost,
                                           'popUpList': popUpList,
                                           'additionalInfoDic': additionalInfoDic,
                                           'monthlyChoice': monthlyChoice,
                                           'tableDic': tableDic,
                                           'requestDic': requestDic})
        return HttpResponse(template.render(context))
    else:



        template = loader.get_template('fabric/cfcalcpage.html')
        context = RequestContext(request, {'listOfNum': numForm,
                                           'dropDowns': dropDowns,
                                           'monthForm': monthForm,
                                           'compare': compare,
                                           'postTrue': postTrue,
                                           'popUpList': popUpList,
                                           'additionalInfoDic': additionalInfoDic})
        return HttpResponse(template.render(context))

def FrontPageView(request):

    privateEdition = models.Product.objects.get(pk=1)
    privateEditionName = privateEdition.name
    privateEditionDescription = privateEdition.description

    global ThePk
    ThePk = 1

    template = loader.get_template('fabric/frontpage.html')
    context = RequestContext(request, {'privateEditionName': privateEditionName,
                                       'privateEditionDescription': privateEditionDescription})
    return HttpResponse(template.render(context))

def handlerCustom404(request):
     return render(request, 'fabric/404.html')

def handlerCustom500(request):
     return render(request, 'fabric/500.html')
