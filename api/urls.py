from rest_framework import routers
from .views import CharacterViewSetResponses

router = routers.DefaultRouter()

router.register(r"character", CharacterViewSetResponses, basename="character")

urlpatterns = router.urls