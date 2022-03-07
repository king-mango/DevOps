from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class test(APIView):
    def get(self, request, *args, **kwargs):
        return Response("OK", status=status.HTTP_200_OK)


class hello(APIView):
    def post(self, request, *args, **kwargs):
        print("Incomming Data")
        print(request.data)
        try:
            name = request.data.get('name') or "You did not provide a name"
            message = "Hello, {}!".format(name)
            return Response(message, status=status.HTTP_200_OK)
        except:
            message = "Something went wrong, please try again!"
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
