from django.shortcuts import render


def loginViwer(request):
    return render (request, ('login\templates\account\login.html'))