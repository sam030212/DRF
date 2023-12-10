from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page")
    return HttpResponse("Home page 1")