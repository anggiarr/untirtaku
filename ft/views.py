from django.shortcuts import render

# Create your views here.
def indexft(request):
    return render(request, 'bukaft.html')