from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination


from .models import Geoname
from .serializers import GeonameSerializer


@api_view(['GET'])
def get_city_by_geonameid(request, pk):
    geoname = Geoname.objects.get(geonameid=pk)
    serializer = GeonameSerializer(geoname)
    return Response(serializer.data)


class GeonameViewSet(viewsets.ModelViewSet):
    queryset = Geoname.objects.all()
    serializer_class = GeonameSerializer()
    pagination_class = LimitOffsetPagination


def get_cities_info(request):
    return render(request)
