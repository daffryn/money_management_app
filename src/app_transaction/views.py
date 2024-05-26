from django.shortcuts import render

# Create your views here.
def page_transaction(request):
    return render(request, 'transaction/index.html')

