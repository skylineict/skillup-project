from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Investment

def investment_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    investments = Investment.objects.filter(user=request.user)
    for investment in investments:
        if investment.is_matured():
            investment.delete_if_matured()  # Delete the investment if matured
        else:
            investment.calculate_profit()

    investments = Investment.objects.filter(user=request.user)  # Refresh the list after deletions

    context = {
        'investments': investments
    }
    return render(request, 'invest.html', context)



def invest(request):
    if request.method == 'POST':
        print('your request is a post one ')
        amount_invested = request.POST.get('amount_invested')
        print("amount is", amount_invested)
        if amount_invested:
            # Create and save the investment
            investment = Investment(
                user=request.user,
                amount_invested=amount_invested,
                start_time=timezone.now(),
            )
            investment.save()
            return redirect('invest')  # Redirect to dashboard after successful investment
    return redirect('invest')