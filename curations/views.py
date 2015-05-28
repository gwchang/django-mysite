from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Collection, Asset

# Create your views here.
class IndexView(generic.ListView):
  #template_name = 'curations/index.html'
  model = Collection
  template_name = 'curations/index.jade'
  context_object_name = 'curations_list'
  
  #def get_queryset(self):
  #  return Collection.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Collection
  template_name = 'curations/detail.jade'

  def get_context_data(self, **kwargs):
    context = super(DetailView, self).get_context_data(**kwargs)
    context['assets_list'] = Asset.objects.filter(collection=self.get_object().id)
    return context
