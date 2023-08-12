```python
from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_generation/lead_list.html', {'leads': leads})

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'lead_generation/lead_detail.html', {'lead': lead})

def new_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm()
    return render(request, 'lead_generation/lead_edit.html', {'form': form})

def edit_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'lead_generation/lead_edit.html', {'form': form})
```