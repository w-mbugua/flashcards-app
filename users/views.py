from django.shortcuts import redirect, render
from .forms import NewFlashCardForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'cards/home.html')

@login_required(login_url='/accounts/login/')
def createcards(request):
    user = request.user
    if request.method == 'POST':
        form = NewFlashCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = user
            card.save()
        return redirect('home')
    else:
        form = NewFlashCardForm()
    return render(request, 'cards/new_card.html', {"form": form})


