from django.shortcuts import render,get_object_or_404,reverse,HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import cateogies, Content,Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth import logout
from .forms import UserRegisterForm,CateogrySearch,ContentSearch

# Create your views here.

class HomeView(ListView):
    template_name = 'homo.html'
    model = Content
    context_object_name = 'Contents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = ContentSearch(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        word = ContentSearch(self.request.GET, queryset=qs)
        return word.qs


class HomeDetail(DetailView):
    template_name = 'detail.html'
    model = Content
    context_object_name = 'Content'


class CateogryView(ListView):
    template_name = 'cateogry.html'
    model = cateogies
    context_object_name = 'passing'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = CateogrySearch(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        word = CateogrySearch(self.request.GET, queryset=qs)
        return word.qs


def DetailCatView(request,id):
    filter = Content.objects.filter(acess=id)
    context = {'cont':filter}

    return render(request,'expand.html',context)

class AddComment(LoginRequiredMixin,CreateView):
    form_class = CommentForm
    template_name = 'comment.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AddComment,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('addcomment', kwargs={'pk': self.kwargs['pk']})

class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return render(request,"permisondenied.html")
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)


class CreateContent(LoginRequiredMixin,LogoutIfNotStaffMixin,CreateView):
    model = Content
    template_name = 'comment.html'
    fields = '__all__'
    success_url = 'Createcontent'
    permission_required = 'is_staff'


class CreateCateogry(LoginRequiredMixin,LogoutIfNotStaffMixin,CreateView):
    model = cateogies
    template_name = 'comment.html'
    fields = ['name','description']
    success_url = 'Createcateogry'
    permission_required = 'is_staff'

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"