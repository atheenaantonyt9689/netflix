import csv
from typing_extensions import runtime
from django.core.management.base import BaseCommand

from myapp.models import Netflix




class Command(BaseCommand):
    help = 'netflixdata'

    def handle(self, *args, **kwargs):

        with open('myapp/netflixoriginals.csv', 'r') as file:

            reader = csv.reader(file)
            for i in reader:
                title=i[0]                
                genre=i[1]
                premiere=i[2]
                runtime=i[3]
                imbb_score=i[4]
                language=i[5]
                

                

                
                obj=Netflix(title=title,genre=genre,premiere=premiere,runtime=runtime,imbb_score=imbb_score,language=language)
                obj.save()

    
    
        
        

