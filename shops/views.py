from multiprocessing import context
from django.shortcuts import render
# from .models import 
# Create your views here.
def get_ice_cream(request ,ice_cream_id ):
    
    context = {
            "ice_cream": {
                'id':'my name',
                'name':'my name',
                'shop':'my shop',
                'stock':'my stock'}

        
    }
    return render(request, 'ice_cream_details.html', context)
    