from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView, DetailView
from django.views.generic import View
from requests import post
from django.views.generic.list import ListView
from .models import Etudiant, Chambre
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EtudiantForm, Chambreform
from django.contrib import messages
from django.db import connection, transaction


# Create your views here.input
def index(request):
    user_list = Etudiant.objects.all()
    query = request.GET.get('q')
    if query:
        user_list = Etudiant.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) |
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(user_list, 3)  # 6 posts per page
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'users': users
    }

    return render(request, 'campus/liste-etudiant.html', context)


class ChambreListView(ListView):
    model = Chambre
    template_name = "campus/liste-chambre.html"
    paginate_by = 1
    context_object_name = 'chambres'
    ordering = ['chambernumber']

    # return render(request, 'campus/liste-chambre.html')


def addStudent(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    form = EtudiantForm()
    return render(request, 'campus/add-etudiant.html', {'form': form})


class StdFormView(FormView):
    form_class = EtudiantForm
    template_name = "campus/add-etudiant.html"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Saved successfuly')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups .. Something went wrong')
        return super().form_invalid(form)


class ChambreFormView(FormView):
    form_class = Chambreform
    template_name = "campus/add-chambre.html"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Saved successfuly')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups .. Something went wrong')
        return super().form_invalid(form)


class EtudiantDetailView(generic.DetailView):
    model = Etudiant
    template_name = "campus/detail-etudiant.html"


def editStudent(request, pk):
    context = {}
    etudiant = get_object_or_404(Etudiant, pk=pk)
    form = EtudiantForm(request.POST or None, instance=etudiant)
    if form.is_valid():
        form.save()
        return redirect('/')
    context["form"] = form
    return render(request, 'campus/edit-etudiant.html', context)


def delete(request, pk, template_name='campus/delete-apprenant.html'):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('/')
    return render(request, template_name, {'etudiant': etudiant})


def detailChambre(request, pk, template_name='campus/detail-chambre.html'):
    context = {}
    studentOfThisChamber = Etudiant.objects.filter(chambre_id=pk).count()
    chambre = get_object_or_404(Chambre, pk=pk)
    context['chambre'] = chambre
    context['studentOfThisChamber'] = studentOfThisChamber
    return render(request, template_name, context)
