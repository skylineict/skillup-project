from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class Postcontent(View):
    def post(self, request):
        return render(request, 'index.html')
    
    def get(self,request):
         return render(request, 'index.html')
        
    