from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from configs.models import Config
from configs.serializers import ConfigSerializer

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Config.objects.all()
        serializer = ConfigSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConfigSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ConfigViewSet(viewsets.ModelViewSet):
#     queryset = Config.objects.all()
#     serializer_class = ConfigSerializer