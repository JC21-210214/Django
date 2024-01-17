from django.http import JsonResponse

def search_view(request):
    try:
        data = request.json()  # 実際のデータ取得方法に合わせて変更してください
        if not data:
            return JsonResponse({'error': '空のリクエストボディ'}, status=400)
        # JSONデータを処理するコード
    except JSONDecodeError as e:
        return JsonResponse({'error': '無効なJSONデータ'}, status=400)
