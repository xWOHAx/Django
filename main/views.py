from django.shortcuts import render
from django.views.generic import ListView
from main.models import Main, Banner

def main(request):
    main = Main.objects.latest('id')
    banners = Banner.objects.all()
    return render(request, 'index.html', {'main': main, 'banners': banners})

class BannerListView(ListView):
    model = Banner
    template_name = 'banners/banner_list.html'
    context_object_name = 'banners'




