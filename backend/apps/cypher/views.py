from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.global_drf_render import CustomRenderer
from apps.cypher.business import CypherHandler

text_param = openapi.Parameter("text", openapi.IN_QUERY, description="Text", type=openapi.TYPE_STRING)
key_param = openapi.Parameter(
    "key",
    openapi.IN_QUERY,
    description="Key",
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_INTEGER),
)


class CypherView(APIView):
    renderer_classes = [CustomRenderer]

    @swagger_auto_schema(manual_parameters=[text_param, key_param])
    def get(self, request, format=None):
        text = request.query_params.get("text", "")
        key = request.query_params.get("key", "").split(",")
        key = [int(i) for i in key]

        if key == [] or text == "":
            return Response({"result": "Invalid params"}, status=400)

        return Response({"result": CypherHandler(text, key).cypher()})


class DecypherView(APIView):
    renderer_classes = [CustomRenderer]

    @swagger_auto_schema(manual_parameters=[text_param, key_param])
    def get(self, request, format=None):
        text = request.query_params.get("text", "")
        key = request.query_params.get("key", "").split(",")
        key = [int(i) for i in key]

        if key == [] or text == "":
            return Response({"result": "Invalid params"}, status=400)

        return Response({"result": CypherHandler(text, key).decypher()})
