from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .forms import CalculatorForm
from .models import Calculation
from .permissions import IsOwnerOrAdmin
from .serializers import CalculationSerializer


# Create your views here.
@login_required
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
                error=error,
                user=request.user,
            )
    else:
        form = CalculatorForm()

    history = Calculation.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'calculator.html', {'form': form, 'result': result, 'history': history, 'error': error})


def clear_history(request):
    if request.method == "POST":
        Calculation.objects.all().delete()
    return redirect('calculator')


class CalculationViewSet(ModelViewSet):
    serializer_class = CalculationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    filterset_fields = ['operation']
    search_fields = ['operation', 'error']
    ordering_fields = ['created_at', 'result']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Calculation.objects.all()
        return Calculation.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
