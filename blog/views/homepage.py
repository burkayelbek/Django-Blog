from django.shortcuts import render

def homepage(request):
    context = {
        'isim': 'Burkay Elbek'
    }
    return render(request,'pages/homepage.html',context=context)