from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutGetView(View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("logar_usuario")

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("logar_usuario")
