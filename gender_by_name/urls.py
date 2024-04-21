from django.contrib import admin
from django.urls import path

from names.views import GetGenderByNameAPIView

urlpatterns = [
    path('api/get_gender_by_name/', GetGenderByNameAPIView.as_view()),
    path('admin/', admin.site.urls),
]
