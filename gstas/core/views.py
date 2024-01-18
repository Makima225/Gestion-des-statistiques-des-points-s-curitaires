from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .forms import EventCreateForm
from .models import *

# Create your views here.

def index(request):

    return render(request, 'index.html')


class EventSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        locality_name = self.request.GET.get('locality', '')

        # Utilisez le champ 'name' de l'objet 'Locality' pour la recherche
        localities = Locality.objects.filter(name__icontains=locality_name)
        events_in_locality = Event.objects.filter(locality__in=localities)
        categories_in_locality = CategoryEvent.objects.filter(event__in=events_in_locality).distinct()

        context['categories_in_locality'] = categories_in_locality 
        return context
    


def events_by_category(request, category_id):
    category = CategoryEvent.objects.get(pk=category_id)
    events = Event.objects.filter(category_event=category)
    
    context = {'category': category, 'events': events}
    
    return render(request, 'show-event.html', context)


def add_event(request):
   form = EventCreateForm(request.POST or None)

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('add-event')
       return render(request, 'add-event.html', {'form':form})
   
   return render(request, 'add-event.html', {'form': form})