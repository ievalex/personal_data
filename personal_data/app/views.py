from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import *
from .forms import *

def home(request):

    #print(request.user.is_authenticated)
    
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def requesters(request):

    requesters = RequesterData.objects.all()

    return render(
        request,
        'app/requesters.html',
        {
            'requesters':requesters,
            'title':'Заявители',
            'is_avaliable': request.user.is_authenticated and request.user.has_perm('app.view_requesterdata'),
            'year':datetime.now().year,
        }
    )

def candidates(request):

    candidates = CandidateData.objects.all()

    return render(
        request,
        'app/candidates.html',
        {
            'candidates':candidates,
            'title':'Кандидаты',
            'is_avaliable': request.user.is_authenticated and request.user.has_perm('app.view_candidatedata'),
            'year':datetime.now().year,
        }
    )

def individuals(request):
    individuals = IndividualBusinessman.objects.all()
    return render(
        request,
        'app/individuals.html',
        {
            'individuals':individuals,
            'title':'Индивидуальные предприниматели',
            'is_avaliable': request.user.is_authenticated and request.user.has_perm('app.view_individualbusinessman'),
            'year':datetime.now().year,
        }
    )


def requester_create(request):
    return requester_edit(request, -1)

def requester_edit(request, id):

    #print(' -------> ', id)

    if id < 0:
        requester = RequesterData()
        title = 'Добавить заявителя'
    else:
        requester = RequesterData.objects.get(id=id)
        title = 'Изменить данные заявителя'
    
    requester_form = RequesterForm(request.POST or None, instance=requester)

    if requester_form.is_valid():
        requester.save()
        return redirect('requesters')

    return render(
            request,
            'app/item_form.html',
            {
                'title': title,
                'form': requester_form
            })

def requester_delete(request, id):
    try:
        requester = RequesterData.objects.get(id=id)
        requester.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except RequesterData.DoesNotExist:
        return HttpResponseNotFound("<h2>Заявитель не найден</h2>")


def candidate_create(request):
    return candidate_edit(request, -1)

def candidate_edit(request, id):

    #print(' -------> ', id)

    if id < 0:
        candidate = CandidateData()
        title = 'Добавить кандидата'
    else:
        candidate = CandidateData.objects.get(id=id)
        title = 'Изменить данные кандидата'
    
    candidate_form = CandidateForm(request.POST or None, instance=candidate)

    if candidate_form.is_valid():
        candidate.save()
        return redirect('candidates')

    return render(
            request,
            'app/item_form.html',
            {
                'title': title,
                'form': candidate_form
            })

def candidate_delete(request, id):
    try:
        candidate = CandidateData.objects.get(id=id)
        candidate.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except CandidateData.DoesNotExist:
        return HttpResponseNotFound("<h2>Кандидат не найден</h2>")


def individual_create(request):
    return individual_edit(request, -1)

def individual_edit(request, id):

    #print(' -------> ', id)

    if id < 0:
        individual = IndividualBusinessman()
        title = 'Добавить индивидуального предпринимателя'
    else:
        individual = IndividualBusinessman.objects.get(id=id)
        title = 'Изменить данные индивидуального предпринимателя'
    
    individual_form = IndividualForm(request.POST or None, instance=individual)

    if individual_form.is_valid():
        individual.save()
        return redirect('individuals')

    return render(
            request,
            'app/item_form.html',
            {
                'title': title,
                'form': individual_form
            })

def individual_delete(request, id):
    try:
        individual = IndividualBusinessman.objects.get(id=id)
        individual.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except IndividualBusinessman.DoesNotExist:
        return HttpResponseNotFound("<h2>Кандидат не найден</h2>")

#-------для API------------------------------------
from rest_framework import viewsets
from .serializers import *

class RequesterViewSet(viewsets.ModelViewSet):
    queryset = RequesterData.objects.all()
    serializer_class = RequesterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = CandidateData.objects.all()
    serializer_class = CandidateSerializer

class IndividualBusinessmanViewSet(viewsets.ModelViewSet):
    queryset = IndividualBusinessman.objects.all()
    serializer_class = IndividualBusinessmanSerializer