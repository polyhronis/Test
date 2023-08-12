```python
from django import forms
from .models import Limo

class LimoForm(forms.ModelForm):
    class Meta:
        model = Limo
        fields = ['name', 'description', 'image', 'availability', 'location']
```