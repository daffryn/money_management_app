from django.shortcuts import render

# Create your views here.
def page_transfer(request):
    return render(request, 'transfer/index.html')

