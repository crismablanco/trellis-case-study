from rest_framework.views import APIView
from rest_framework.response import Response
from .services import NumbersService
from .serializers import ConverterSerializer


class NumberConverterToWordsView(APIView):
    def get_number_in_words(self, number: int, and_word: str = "") -> Response:
        service = NumbersService(and_word=and_word)
        num_in_english = service.convert(number=int(number) if number.isdigit() else -1)
        status_code = 200 if num_in_english else 500
        raw_data = dict(
            status="ok" if num_in_english else "fail", num_in_english=num_in_english
        )
        serialized_data = ConverterSerializer(instance=raw_data).data
        return Response(serialized_data, status=status_code)

    def post(self, request):
        requested_number = request.data.get("number", "")
        and_word = request.data.get("and_word", "")

        return self.get_number_in_words(number=requested_number, and_word=and_word)

    def get(self, request):
        requested_number = request.GET.get("number", "")
        and_word = request.GET.get("and_word", "")

        return self.get_number_in_words(number=requested_number, and_word=and_word)
