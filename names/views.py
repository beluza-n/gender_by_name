from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Man, Woman


class GetGenderByNameAPIView(APIView):
    """
    Determines gender by name.
    """

    def post(self, request):
        id = request.data["id"]
        name = request.data["name"]
        if not name.isalpha():
            return Response(
                    {'детали': 'Имя должно содержать только буквы.'},
                    status=status.HTTP_400_BAD_REQUEST)
        gender = ''
        try:
            Man.objects.get(name=name)
            gender = 'Мужчина'
        except Man.DoesNotExist:
            try:
                Woman.objects.get(name=name)
                gender = 'Женщина'
            except Woman.DoesNotExist:
                return Response(
                    {'детали': 'Имя не найдено.'},
                    status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {'id': id,
             'name': name,
             'gender': gender
             }
            ) 
