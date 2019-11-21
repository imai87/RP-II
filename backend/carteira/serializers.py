from rest_framework_mongoengine import serializers
from .models import Atual, Ativos, Historico


class AtualSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Atual
        fields = '__all__'

class AtivosSerializer(serializers.DocumentSerializer):
    
    class Meta:
        model = Ativos
        fields = '__all__'

class HistoricoSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Historico
        fields ='__all__'