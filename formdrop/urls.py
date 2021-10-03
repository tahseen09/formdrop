from forms.views import submit, index

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/submit/<id>', submit),
    path('', index)
]
