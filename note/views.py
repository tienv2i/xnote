from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'note/index.html', {})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Yêu cầu token hợp lệ

    def get(self, request):
        return Response({"message": "Xin chào, bạn đã đăng nhập thành công!"})