from django.contrib import admin
from django.urls import path, include
from storage import views

urlpatterns = [
    path('', include('storage.urls')),
    path('admin/', admin.site.urls),
    path('api/is_exist/', views.ClientList.as_view()),  # method GET
    path('api/delete-sleeps/<int:pk>/', views.ClientDeleteClientSleeps.as_view()),  # method PUT
]
