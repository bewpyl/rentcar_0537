from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from .models import Car,Rent,Return
from .models import Person
from .forms import PersonForm,RentForm,ReturnForm,CarForm


# Create your views here.

def home(request):
	return render(request,'home.html')

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='creates.html'
	form_class = PersonForm
	success_url = '/admin'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'
 
class ListCarView(ListView):
    model = Car
    template_name='carlist.html'

class ListRentView(ListView):
    model = Rent
    template_name='rentlist.html'

class CreateRentView(CreateView):
	queryset = Rent()
	template_name='rent.html'
	form_class = RentForm
	success_url = '/admin'

class CreateReturnView(CreateView):
	queryset = Return()
	template_name='return.html'
	form_class = ReturnForm
	success_url = '/admin'



#def some_name(request):
 #   rent_instance = Rent.objects.create(name='test')
  #  return render(request, 'some_name.html.html')
