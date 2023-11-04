"""
URL configuration for escapegameapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from escapegame.views import GameViewSet, StepViewSet, ScenarioViewSet, ScenarioNodeViewSet, ClueViewSet, GamePlayViewSet, ScenarioPlayViewSet, StepPlayViewSet, ScenarioNodePlayViewSet, CluePlayViewSet
from authentication.views import SignUpView, GetUserView

# URLs require slash
router = routers.SimpleRouter()

router.register('game', GameViewSet, basename = 'game')
router.register('step', StepViewSet, basename = 'step')
router.register('scenario', ScenarioViewSet, basename = 'scenario')
router.register('scenario_node', ScenarioNodeViewSet, basename = 'scenario_node')
router.register('clue', ClueViewSet, basename = 'clue')

router.register('play/game', GamePlayViewSet, basename = 'game_play')
router.register('play/scenario', ScenarioPlayViewSet, basename = 'scenario_play')
router.register('play/step', StepPlayViewSet, basename = 'step_play')
router.register('play/scenario_node', ScenarioNodePlayViewSet, basename = 'scenario_node_play')
router.register('play/clue', CluePlayViewSet, basename = 'clue_play')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignUpView.as_view(), name="sign_up"),
    #path('api/game/<int:game_id>', GameDetailsAPIView.as_view(), name = 'game_details'),
    #path('api/game/', GameListAPIView.as_view(), name = 'game_list'),
    path('api/user/<int:user_id>/', GetUserView.as_view(), name = 'get_user_info')
]