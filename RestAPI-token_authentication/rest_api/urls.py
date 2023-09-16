from rest_framework.routers import SimpleRouter
from rest_api.views import RegisterModelViewSet
from django.urls import path

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('register', RegisterModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls