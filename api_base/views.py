from django.shortcuts import render ,get_object_or_404
from .models import  Article
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
from  .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from  django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from  rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework import viewsets
# Create your views here.

# normal api_views.

# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         snippets = Article.objects.all()
#         serializer = ArticleSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)
#

# function-base api_views

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         article =Article.objects.all()
#         serializer = ArticleSerializer(article,many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','POST','PUT','DELETE'])
# def article_details(request ,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class-base api_views

# class ArticleList(APIView):
#     def get(self,request,format =None):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article,many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetails(APIView):
#     def get_object(self,pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk ,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self,request,pk,format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class-base api_views plus Mixins

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,
#                   mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def destroy(self,request,*args,**kwargs):
#         return self.destroy(request, *args, **kwargs)


# class-base api_views plus Generic


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# Basic and Session Authentication Class Base View.

# class ArticleAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     lookup_field = 'pk'
#
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self,request,pk=None):
#         if pk :
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#     def put(self,request,pk=None):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#

# Token Authentication .

# class ArticleAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     lookup_field = 'pk'
#
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self,request,pk=None):
#         if pk :
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#     def put(self,request,pk=None):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# ViewSets & Routers

# class  ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         article = Article.objects.all()
#         serializer =ArticleSerializer(article,many=True)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request,pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def update(self,request,pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GenericViewsets & Routers

# class GenericViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()


# Viewsets And Model Viewsets
class GenericViewsets(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

