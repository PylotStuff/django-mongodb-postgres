from django.http.response import JsonResponse
from .tasks import create_random_posts


def post_generator(request):
    create_random_posts.delay()
    return JsonResponse({"success": True})
