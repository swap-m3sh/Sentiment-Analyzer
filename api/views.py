from django.shortcuts import render
from .api import fetchComments
from .sentiment import analyzer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.

@api_view(['GET','POST'])
def sentimentAnalyzer(request):
    if request.method == 'GET':
        msg = "Welcome to Sentiment Analyzer"
        res = {'message': msg}
        return Response(res)

    if request.method=="POST":
        res = json.loads(request.body.decode("utf-8"))
        url = res['url']
        comments = fetchComments(url)
        results = analyzer(comments)
        jsonres = json.loads(results)
        return Response(jsonres)
