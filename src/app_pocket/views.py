from django.shortcuts import render

# Create your views here.
def page_pocket(request):
    return render(request, 'pocket/index.html')

