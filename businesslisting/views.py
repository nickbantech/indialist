from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import List

def home(request):

	context ={

	     'listing': List.objects.all()
	 }

	return render(request,'businesslisting/home.html',context)

class BizListView(ListView):
	model = List
	template_name = 'businesslisting/home.html'
	context_object_name = 'listing'
	ordering = ['-date_posted']

class BizDetailView(DetailView):
	model = List
	
class BizCreateView(LoginRequiredMixin, CreateView):
	model = List
	fields = ['name','description','website','contact','email','address','pincode']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class BizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = List
	fields = ['name','description','website','contact','email','address','pincode']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		list = self.get_object()
		if self.request.user == list.author:
			return True

		return False	

class BizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = List
	success_url ='/'

	def test_func(self):
		list = self.get_object()
		if self.request.user == list.author:
			return True

		return False	




def about(request):
	return render(request,'businesslisting/about.html')

def category(request):
	return HttpResponse('<h1>Categories</h1>')	


