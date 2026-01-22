from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Avg



from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API V1
"""
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    # queryset = Curso.objects.all() (para retornar a média cai no N+1 problem)
    queryset = Curso.objects.annotate(
        media_avaliacoes=Avg('avaliacoes__avaliacao')
    )
    serializer_class = CursoSerializer


    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class_page_size = 6
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['get'],
        url_path=r'avaliacoes/(?P<avaliacao_pk>[^/.]+)'
    )
    def avaliacao(self, request, pk=None, avaliacao_pk=None):
        curso = self.get_object()

        avaliacao = curso.avaliacoes.filter(pk=avaliacao_pk).first()
        if avaliacao is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer










