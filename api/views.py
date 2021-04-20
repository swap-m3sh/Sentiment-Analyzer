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
        msg1 = "Welcome to Sentiment Analyzer"
        msg2 = "This is Json example, you can send as POST request"
        msg3 = "Change the url value to your youtube video url"        
        msg4 = "https://www.youtube.com/watch?v=paste_the_link_here"
        msg5 = "The ML based Analyzer will classify comments as Positive Comment or Negative Comment"
        
        res = {'greeting': msg1, 'description':msg2, 'howtouse' :msg3, 'url':msg4, 'working':msg5 }
        return Response(res)

    if request.method=="POST":
        res = json.loads(request.body.decode("utf-8"))
        url = res['url']
        comments = fetchComments(url)
        results = analyzer(comments)
        jsonres = json.loads(results)
        return Response(jsonres)
