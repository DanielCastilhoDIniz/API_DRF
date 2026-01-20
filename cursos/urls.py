from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    AvaliacaoAPIView,
    CursosAPIView,
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliacaoViewSet)


router = SimpleRouter()
router.register('cursos', CursoViewSet, basename='cursos')
router.register('avaliacoes', AvaliacaoViewSet, basename='avaliacoes')


urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos-list-create'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso-detail'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes-list-create'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

