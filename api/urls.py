from django.urls import path
from api.views import EmployeeAPIView,EmployeeDetailAPIView
urlpatterns = [
    path('', EmployeeAPIView.as_view()),
    path('<int:id>/', EmployeeDetailAPIView.as_view()),
]
