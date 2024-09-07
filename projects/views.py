from django.http import JsonResponse
from django.views import View
from .models import Company

# Create your views here.

class CompanyView(View):

    def get(self,request):
        companies= list(Company.objects.values())
        if len(companies)>0:
            datos={'message':"Succes",'companies':companies}
        else:
            datos={'message':"companies not found ..."}
        return JsonResponse(datos)

    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass