from django.shortcuts import render

# Create your views here.
def taskViwer(request):
    return render (request, ('task/static/task.html'))
