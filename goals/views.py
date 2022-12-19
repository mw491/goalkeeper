from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Goal


@require_http_methods(["GET", "POST"])
@csrf_exempt
def goals(request):
    if request.method == "GET":  # list all goals
        goals = Goal.objects.all()
        goals_json = serializers.serialize("json", goals)
        return HttpResponse(goals_json, content_type="application/json")
    elif request.method == "POST":  # add goal
        title = request.POST.get("title")
        date = request.POST.get("date")
        Goal.objects.create(title=title, completed=False, date=date).save()
        return HttpResponse("Created Successfully")


@csrf_exempt
def goal(request, id):
    goal = Goal.objects.get(id=id)
    if request.method == "GET":  # list goal information
        return JsonResponse(
            {
                "id": goal.id,
                "title": goal.title,
                "completed": goal.completed,
                "date": goal.date,
            }
        )
    elif request.method == "POST":  # update goal
        if request.POST.get("title"):
            goal.title = request.POST.get("title")
        if request.POST.get("completed"):
            goal.title = request.POST.get("completed")
        if request.POST.get("date"):
            goal.title = request.POST.get("date")
        goal.save()
        return HttpResponse("Edited Successfully")
    elif request.method == "DELETE":  # delete goal
        goal.delete()
        return HttpResponse("Deleted Sucessfully")
