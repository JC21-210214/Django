from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
import requests
import json  # 追加

class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Webapp/top.html')
    
top_page = SampleView.as_view()

def search_view(request):
    search_endpoint = 'https://new-sotuken.search.windows.net'
    api_key = 'HZXxm9swg3Dnve7aZVelgyIeXcRfLERmoowHnlZxjCAzSeAdfGSy'
    index_name = 'book-search'
    search_text = '*'

    try:
        response = requests.get(
            f'{search_endpoint}/book-search/{index_name}/"https://new-sotuken.search.windows.net"{search_text}',
            headers={'Content-Type': 'application/json', 'HZXxm9swg3Dnve7aZVelgyIeXcRfLERmoowHnlZxjCAzSeAdfGSy': api_key}
        )
        response.raise_for_status()  # HTTPエラーチェック

        data = response.json()
        search_results = data.get('value', [])
        context = {}
        if search_results:
            first_result = search_results[0]
            context = {
                'book_author': first_result.get('BookAuthor', ''),
                'release_date': first_result.get('Release_Date', ''),
                'book_name': first_result.get('BookName', ''),
                'rating': first_result.get('Rating', ''),
                'book_genre': first_result.get('BookGenre', ''),
            }
        return render(request, 'Webapp/results.html', context)
    except requests.exceptions.RequestException as e:
        # エラーログなどを記録する
        print(f"Error in search_view: {e}")
        # 例外が発生した場合の適切なレスポンスを返す
        return HttpResponse("An error occurred while processing the request.", status=500)
