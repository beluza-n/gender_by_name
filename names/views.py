from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_spectacular.utils import (
    extend_schema, extend_schema_view)

from .serializers import (
    DummyGenderRequestSerializer,
    DummyGenderResponseSerializer,
    DummyDetailSerializer
    )


from .models import Man, Woman


@extend_schema(tags=["Get gender by name"],
               request=DummyGenderRequestSerializer,
               responses={
                   status.HTTP_200_OK: DummyGenderResponseSerializer,
                   status.HTTP_400_BAD_REQUEST: DummyDetailSerializer,
                   status.HTTP_404_NOT_FOUND: DummyDetailSerializer
                   }
               )
@extend_schema_view(
    post=extend_schema(
            summary="Get gender by name",
            description="""POST request id and name in json format.
            Recieve gender ("Мужчина" for male and "Женщина" for female)."""
            ))
class GetGenderByNameAPIView(APIView):
    """
    Determines gender by name.
    """

    def post(self, request):
        id = request.data["id"]
        name = request.data["name"]
        if not name.isalpha():
            return Response(
                    {'detail': 'Name must contain only letters.'},
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
                    {'detail': 'Name not found.'},
                    status=status.HTTP_404_NOT_FOUND)
        return Response(
            {'id': id,
             'name': name,
             'gender': gender
             },
            status=status.HTTP_200_OK)
