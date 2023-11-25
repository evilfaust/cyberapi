from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('rangplayer/', views.RangPlayerList.as_view()),
    path('gamedota2/', views.GameDota2List.as_view()),
    path('game-stats/<int:game_id>/', views.GameDota2GameList.as_view(), name='game-stats'),

]

urlpatterns = format_suffix_patterns(urlpatterns)