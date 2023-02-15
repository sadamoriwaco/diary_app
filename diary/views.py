from os import terminal_size
import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from .forms import DiaryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Diary
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'SUBMIT')
        # logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin,generic.ListView):
    model = Diary
    template_name = 'list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        print(diaries)
        return diaries

class DetailView(generic.DetailView):
    model = Diary
    slug_field = "title"
    slug_url_kwarg = 'title'

class DiaryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name = 'detail.html'
    # pk_url_kwarg = 'id'

class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    model =Diary
    template_name = 'create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:list')

    def form_valid(self,form):
        diary = form.save(commit=False)

        diary.user = self.request.user
        # diary.user = self.request.user.id
        diary.save()
        messages.success(self.request,'SUBMIT')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,'ERROR')
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Diary
    template_name='update.html'
    form_class=DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'UPDATED')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,'ERROR')
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Diary
    template_name = 'delete.html'
    success_url = reverse_lazy('diary:list')

    def delete(self,request,*args,**kwargs):
        messages.succcess(self.request,"DELETED")
        return super().delete(request,*args,**kwargs)