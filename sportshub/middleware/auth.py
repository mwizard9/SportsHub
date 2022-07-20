from django.shortcuts import redirect, render

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.user)
        
        if not request.user:
           return redirect('login')

        response = get_response(request)
        return response

    return middleware