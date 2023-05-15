from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 장고 안에 만들어져 있는 기능을 가져옴

def calculator(request) :
    #return HttpResponse('계산기 기능 구현 시작')
    
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    if (operators == '+') :
        result = int(num1) + int(num2)
    elif (operators == '-') :
        result = int(num1) - int(num2)
    elif (operators == '*') :
        result = int(num1) * int(num2)
    elif (operators == '/') :
        result = int(num1) / int(num2)
    else :
        result = 0
     
    return render(request, 'calculator.html', {'result': result})

