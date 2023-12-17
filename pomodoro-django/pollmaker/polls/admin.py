from django.contrib import admin
from .models import Question

# Register your models here.
# Models added here will be modifiable on the admin view
admin.site.register(Question)
