from rest_framework import status
from .models import Product
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSeralizer
from rest_framework.permissions import IsAuthenticated



class ProductCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({
                "msg": "mahsulot qo'shildi",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'error': "Nimadir hato ketti"
        }, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.author != request.user:
            return Response({
                "error" : "Faqat o'zingizni mahsilotingizni oedit qila olasiz"
            })

        serializer = ProductSeralizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg" : "O'zgartirildi",
                'data' : serializer.data
            })
        return Response({
            "error" : "Xatolik"
        })

    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.author != request.user:
            return Response({
                "error" : "Faqat o'zingizni mahsilotingizni oedit qila olasiz"
            })

        serializer = ProductSeralizer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg" : "O'zgartirildi",
                'data' : serializer.data
            })
        return Response({
            "error" : "Xatolik"
        })




class ProductDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.author != request.user:
            return Response({
                'msg' : "Bu sizning mahsulot emas"
            })
        product.delete()
        return Response({
            "msg" : f"{product.name} ochirildi"
        })


class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.filter(author=request.user)

        serializer = ProductSeralizer(products, many=True)
        return Response({
            "data" : serializer.data
        })


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def detail(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        serializer = ProductSeralizer(product)
        return Response({
            'data' : serializer.data
        })