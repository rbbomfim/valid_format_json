from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class FormatJson(APIView):
    def post(self, request, *args, **kwargs):
        json_data = request.data  # Pega os dados diretamente do corpo da requisição
        format_type = request.query_params.get('format_type', 'pretty')

        try:
            # No formato "pretty", usa o Response do DRF para formatação automática
            if format_type == 'pretty':
                return Response(json_data, status=200)
            # No formato "compact", usa json.dumps e retorna diretamente via HttpResponse
            elif format_type == 'compact':
                compact_json = json.dumps(json_data, separators=(',', ':'))
                return HttpResponse(compact_json, content_type='application/json', status=200)
            else:
                return Response({'error': 'Invalid format type specified'}, status=400)
        except TypeError:
            return Response({'error': 'Invalid JSON'}, status=400)