from django.shortcuts import render

# Create your views here.
def villagebreader(request):
    return render(request, "Article/VillagerBreader.html")