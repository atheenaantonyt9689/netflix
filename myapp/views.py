from typing import Counter
from django.shortcuts import render
from .models import Netflix

from django.views import View

        
# Create your views here.
class HomePageView(View):
    model=Netflix
    template_name='core_section/test.html'

    def get(self,request,*args,**kwargs):
        
        dataset=Netflix.objects.all()       

        context={
            'dataset':dataset
        }

        return render(request,"core_section/filter.html",context)
        
    def post(self,request,*args,**kwargs):
        genre=request.POST.get('genre')
        language=request.POST.get('language')
        print(language)
       
        search_result=Netflix.objects.filter(genre=genre,language=language)
        count_search=Netflix.objects.filter(genre=genre,language=language).count()
        

        print("ndbemnemjn",search_result)
        

        
        
        context={
            'search_result':search_result,
            'count_search':count_search
           

        }
       
        return render(request,"core_section/filter.html",context)
    




