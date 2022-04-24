from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm

from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import News, Category
from .utils import MyMixin

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             '', ['muzaffarbeksaidahmedov@gamil.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Xabar yuborildi!!!')
                return redirect('contact')
            else:
                messages.error(request, 'Yuborishda xatolik!!!')
        else:
            messages.error(request, "Ma'lumot noto'ri kiritilgan")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
            return redirect('login')
        else:
            messages.error(request, "Ro'yxatdan o'tishda xatolik")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'test.html', {'page_obj': page_objects})



class BoshNews(MyMixin, ListView):
    model = News
    template_name = 'home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Bosh sahifa'}
    mixin_prop = 'Hello World'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Bosh sahifa')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)



# class NewsByCategory(ListView):
#     model = News
#     template_name = 'home_news_list.html'
#     context_object_name = 'news'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = Category.objects.get(slug=self.kwargs['slug'])
#         return context

class ViewNews(DeleteView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'add_news.html'
    raise_exception = True
    # success_url = reverse_lazy('home')

# def index(request):
#     news= News.objects.all().order_by('-created')
#     context = {
#         'news':news,
#         'title': 'Yangiliklar ro`yxati',
#     }
#     return render(request, 'index.html', context)
#
def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category=category)
    context = {
        'category': category,
        'news': news,
    }
    return render(request, 'index.html', context)

# def view_news(request, slug):
#     news = get_object_or_404(News, slug=slug)
#     return render(request, 'view_news.html', {'news': news})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_news')
#     else:
#         form = NewsForm()
#     return render(request, 'add_news.html', {'form': form})


