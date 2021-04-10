from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import createpost as cp
from rest_framework import decorators, permissions
from rest_framework.decorators import api_view
from .serialization import serialization
from django.shortcuts import get_object_or_404 as getobj
# Create your views here.


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def createpost(request):
    print(request)
    postTittle = request.data['postTitle']
    post = request.data['post']
    db = cp(postTittle=postTittle, post=post)
    db.save()
    data = {"Post titile": postTittle, "post": post}

    return render(request, 'createpost.html')


# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
def readpost(request):
    # data = cp.objects.all()
    # serializer = serialization(data, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return render(request, 'readpost.html')

    class Meta:
        db_table = 'posts_createpost'
        ordering = ['-timestamp']
        verbose_name = 'create post'
        verbose_name_plural = 'create posts'


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def delete(request):
    id = int(request.data['id'])
    postTitle = request.data['post title']
    obj = getobj(cp, id=id)
    obj.delete()
    return JsonResponse("post deleted", safe=False)
