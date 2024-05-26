from django.shortcuts import render

# Create your views here.
def page_dashboard(request):
    return render(request, 'dashboard/index.html')
