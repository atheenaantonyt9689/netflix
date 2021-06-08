from django.shortcuts import render
from .models import Netflix

from django.views import View
class FilterView(View):
    model=Netflix
    template_name='core_section/filter.html'

    def get(self,request,*args,**kwargs):
        
        all=Netflix.objects.all()

        print(all)
            

        context={'all':all
        }

        return render(request,"core_section/home.html",context)
        
# Create your views here.
class HomePageView(View):
    model=Netflix
    template_name='core_section/filter.html'

    def get(self,request,*args,**kwargs):
        
        dataset=Netflix.objects.all()

        print(dataset)
            

        context={'dataset':dataset
        }

        return render(request,"core_section/filter.html",context)
        
    def post(self,request,*args,**kwargs):

        xx=request.POST.get("genre")
        
        context={

        }
       
        return render(request,"core_section/home.html",context)
    




