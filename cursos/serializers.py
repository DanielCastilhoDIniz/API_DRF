from rest_framework import serializers




from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


    def validate_curso(self, value):
        if not value.active:
            raise serializers.ValidationError(
                'Curso inativo não pode receber avaliações'
            )
        return value


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
            'active',
        )




class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship     # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  view_name='avaliacoes-detail',
    #                                                  read_only=True)

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # media_avaliacoes = serializers.SerializerMethodField() ( n+1 problem )
    media_avaliacoes = serializers.SerializerMethodField()

    # resolve o N+1 desde que use annotate na view
    def get_media_avaliacoes(self, obj):
        if obj.media_avaliacoes is None:
            return 0
        return round(obj.media_avaliacoes * 2) / 2


    class Meta:
        model = Curso
        fields = (
            'id',
            'title',
            'url',
            'created',
            'updated',
            'active',
            'avaliacoes',
            'media_avaliacoes'
        )

