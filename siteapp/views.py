from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import *
from .models import Countries

menu = [
    {'title': "Main", 'url_name': "main"},
    {'title': "About us", 'url_name': "about"},
    {'title': "Add post", 'url_name': "addpage"},
]


def index(request):
    context = {
        'posts': Countries.objects.all(),
        'menu': menu,
    }
    return render(request, "siteapp/index.html", context=context)


def about(request):
    context = {
        'posts': Countries.objects.all(),
        'menu': menu,
    }
    return render(request, "siteapp/about.html", context=context)

class ContriesAdd(View):

    def get(self, request):
        form = CountriesForm()
        context = {
            'form': form,
            'posts': Countries.objects.all(),
            'menu': menu,
        }
        return render(request, 'siteapp/addpage.html', context=context)

    def post(self, request):
        bound_forms = CountriesForm(request.POST)

        if bound_forms.is_valid():
            new_post = bound_forms.save()
            return redirect('main')
        context = {
            'form': bound_forms,
            'posts': Countries.objects.all(),
            'menu': menu,
        }
        return render(request, 'siteapp/addpage.html', context=context)

# def addpage(request):
#     response = ""
#     if request.method == "POST":
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             try:
#                 Countries.objects.create(**form.cleaned_data)
#                 return redirect('main')
#             except:
#                 form.add_error(None, "Error")
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#         'posts': Countries.objects.all(),
#         'menu': menu,
#         'response': response,
#     }
#     return render(request, "siteapp/addpage.html", context=context)

def show_post(request, pk):
    post = get_object_or_404(Countries, pk=pk)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'images': post.photo,
    }

    return render(request, 'siteapp/post.html', context=context)

def lamp(request):
    return render(request, 'siteapp/lamp.html')


def handling_404(request, exception):
    return render(request, 'siteapp/404.html')
