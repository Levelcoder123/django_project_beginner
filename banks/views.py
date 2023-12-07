from django.views.generic import ListView

from .models import Bank


class BankView(ListView):
    model = Bank
    template_name = 'banks.html'
