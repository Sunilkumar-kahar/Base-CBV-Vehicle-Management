from django.http import HttpResponseForbidden

ALLOW_IP_ADDR = ['127.0.0.1']

class IPFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ALLOW_IP_ADDR:
            return HttpResponseForbidden('Access Denied')
        return self.get_response(request)