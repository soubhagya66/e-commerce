from django.shortcuts import render

def basket_summary(request):
    return render(request, 'store/baskets/summary.html')
