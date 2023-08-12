```python
from django.shortcuts import render
from .models import Limo, Tracking

def get_limo_data(request):
    limos = Limo.objects.all()
    return render(request, 'limo_list.html', {'limos': limos})

def get_limo_detail(request, id):
    limo = Limo.objects.get(id=id)
    return render(request, 'limo_detail.html', {'limo': limo})

def get_tracking_data(request, limo_id):
    tracking = Tracking.objects.filter(limo_id=limo_id)
    return render(request, 'limo_tracking.html', {'tracking': tracking})
```