from os import terminal_size
import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin,generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objacts.filter(user=self.request.user).oder_by('-created_at')
        return diaries

class DetailView(genneric.DetailView):
    model = Post
    slug_field = "title"
    slug_url_kwarg = 'title'

class DiartDetailView(LoginRequiredMixin,genneric.DetailView):
    model = Diary
    template_name = 'diary_detil.html'