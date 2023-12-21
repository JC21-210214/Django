from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
import requests

class SampleView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'Webapp/top.html')
top_page = SampleView.as_view()


def search_view(request):
    search_endpoint = 'https://sotuken-beta.search.windows.net'
    api_key = 'RvICL223LXinONIZB3GHMoQTP5MfmCUmoH4iav37B3AzSeA918fw'
    index_name = 'book-search'
    search_text = '若い男と老婆が揉める'

    response = requests.get(
        f'{search_endpoint}/indexes/{index_name}/docs/search?api-version=2020-06-30&search={search_text}',
        headers={'Content-Type': 'application/json', 'api-key': api_key}
    )

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