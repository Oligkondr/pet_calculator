from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CalculatorForm


def calculator_view(request):
    result = None
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
                    result = "Zero division!"
    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form, 'result': result})
