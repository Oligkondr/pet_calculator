from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .forms import CalculatorForm
from .models import Calculation


def calculator_view(request):
    result = None
    error = None

    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operation = form.cleaned_data['operation']

            if operation == 'add':
                result = number1 + number2
            elif operation == 'sub':
                result = number1 - number2
            elif operation == 'mul':
                result = number1 * number2
            elif operation == 'div':
                if number2 != 0:
                    result = number1 / number2
                else:
                    error = "Zero division!"

            Calculation.objects.create(
                number1=number1,
                number2=number2,
                operation=operation,
                result=result,
                error=error
            )
    else:
        form = CalculatorForm()

    history = Calculation.objects.order_by('-created_at')

    return render(request, 'calculator.html', {'form': form, 'result': result, 'history': history, 'error': error})

def clear_history(request):
    if request.method == "POST":
        Calculation.objects.all().delete()
    return redirect('calculator')
