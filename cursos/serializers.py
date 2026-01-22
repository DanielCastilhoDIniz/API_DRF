from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'created',
            'updated',
            'active'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship     # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  view_name='avaliacoes-detail',
    #                                                  read_only=True)

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Curso
        fields = (
            'id',
            'title',
            'url',
            'created',
            'updated',
            'active',
            'avaliacoes'
        )
