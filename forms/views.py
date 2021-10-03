import json

from .models import Form, Content

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit(request, id):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Only POST HTTP Method Allowed"})
    form = Form.objects.get(id=id)
    body = request.POST or request.body
    if isinstance(body, (bytes, str)):
        body = json.loads(body)
    elif not isinstance(body, dict):
        if form.failure_redirect:
            return redirect(form.failure_redirect)
        return JsonResponse({"success": False, "message": "Data Not Recognized"})
    Content.objects.create(form=form, body=body)
    if form.success_redirect:
        return redirect(form.success_redirect)
    return JsonResponse({"success": True, "message": "We have received your response. Thankyou."})


def index(request):
    return render(request, 'index.html')
