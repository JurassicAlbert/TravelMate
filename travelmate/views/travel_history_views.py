from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..forms.travel_history_form import TravelHistoryForm
from ..models.travel_history import TravelHistory


class TravelHistoryView:
    @login_required
    def history_list(request):
        history = TravelHistory.objects.filter(user=request.user)
        return render(request, 'travel_history.html', {'history': history})

    @login_required
    def add_history(request):
        if request.method == 'POST':
            form = TravelHistoryForm(request.POST)
            if form.is_valid():
                history = form.save(commit=False)
                history.user = request.user
                history.save()
                return redirect('history_list')
        else:
            form = TravelHistoryForm()
        return render(request, 'add_travel_history.html', {'form': form})

    @login_required
    def delete_history(request, history_id):
        history = get_object_or_404(TravelHistory, id=history_id, user=request.user)
        history.delete()
        return redirect('history_list')
