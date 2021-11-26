from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .models import liked_data
from django.http import HttpResponse, JsonResponse
from django.db.models import Q


# Create your views here.


@login_required
def get_data(request):

    username = request.user.username
    like = request.POST["likedis"]
    post_i = request.POST["idval"]
    source = request.POST["source"]
    user_i = request.user.id
    counter = apps.get_model("bus", source)

    if like in "on":
        print("iam on")
        # create liked data if its does not exists with user id
        liked = liked_data.objects.filter(Q(user_id=user_i), Q(post_id=post_i))
        print(liked, "likedata exists")
        # create liked data if its does not exists with user id
        #like turned on
        if not liked:  # createting if user id  & post id doesnot exists
            liked_data.objects.create(user_id=user_i, post_id=post_i).save()

        count = counter.objects.only("likes_count").get(id=post_i)
        count.likes_count = count.likes_count + 1
        count.save()

    else:
        #like turned off
        liked_data.objects.filter(
            Q(user_id=user_i), Q(post_id=post_i)).delete()
        count = counter.objects.only("likes_count").get(id=post_i)
        count.likes_count = count.likes_count - 1
        count.save()

    count = counter.objects.only("likes_count").get(id=post_i)

    return JsonResponse({
        "data": count.likes_count
    })

def home2(request):
    return render(request,"no.html")
