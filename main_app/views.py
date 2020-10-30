from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Claim
from .forms import ClientForm, ClaimForm

def home(request):
    return HttpResponse('it is working')

def about(request):
    return render(request, 'about.html')

# client views
def client_index(request):
    clients = Client.objects.all()
    return render(request, 'clients/index.html', {'clients': clients})

def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/detail.html', {'client': client})

def add_client(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            new_client = client_form.save() # (commit=False)? just for user format?
            return render(request, 'clients/detail.html', {'client': new_client})
    else:
        form = ClientForm()
        return render(request, 'clients/add.html', {'form': form})

def delete_client(request, client_id):
    Client.objects.get(id=client_id).delete()
    return render(request, 'clients/index') # why no .html? compare to others

def edit_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            updated_client = client_form.save()
            return redirect('client_detail', updated_client.id)
    else:
        form = ClientForm(instance = client)
        return render(request, 'clients/edit.html', {'form': client_form, 'client': client})

# claim views
def claim_index(request):
    claims = Claim.objects.all()
    return render(request, 'claims/index.html', {'claims': claims})

def claim_detail(request, claim_id):
    claim = Claim.objects.get(id=claim_id)
    return render(request, 'claims/detail.html', {'claim': claim})

def add_claim(request):
    if request.method == 'POST':
        claim_form = ClaimForm(request.POST)
        if claim_form.is_valid():
            new_claim = claim_form.save() # (commit=False)? just for user format?
            return render(request, 'claim/detail.html', {'claim': new_claim})
    else:
        form = ClaimForm()
        return render(request, 'claims/add.html', {'form': form})

def delete_claim(request, claim_id):
    Claim.objects.get(id=claim_id).delete()
    return render(request, 'claims/index.html')

def edit_claim(request, claim_id):
    claim = Claim.objects.get(id=claim_id)
    if request.method == 'POST':
        claim_form = ClaimForm(request.POST)
        if claim_form.is_valid():
            updated_claim = claim_form.save()
            return redirect('claim_detail', updated_claim.id)
    else:
        claim_form = ClaimForm(instance = claim)
        return render(request, 'claims/edit.html', {'form': claim_form, 'claim': claim})
