from django.shortcuts import render, redirect
from main.models import Information
from django.contrib import messages


# user home page
def home(request):
    return render(request, 'index.html')


# dashboard section
def dashboard(request):
    inputBikeNumber = request.GET.get('BikeNumber')
    x = checkifBikeExist(inputBikeNumber)
    if x == 1:
        allUserInfo = Information.objects.get(BikeNo=inputBikeNumber)
        context = {
            'data': allUserInfo,
        }
        return render(request, 'dashboard.html', context)
    else:
        messages.error(request, "यो नमब्र सँग सम्बंधित कुनै पनि डाटा हामी सँग छैन क्रिपैया अर्को नम्बर हाल्नु होस ")
        return redirect('home')


def checkifBikeExist(inputBikeNumber):
    try:
        a = Information.objects.get(BikeNo=inputBikeNumber)
        return 1
    except:
        return 2