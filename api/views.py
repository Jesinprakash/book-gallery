from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Book,Review

from api.serializer import BookSerializer,ReviewSerializer

from rest_framework import viewsets

from rest_framework import authentication,permissions

from rest_framework import generics

from rest_framework.decorators import action    #this decorator used to check the id in url or not
class BookCreateListView(APIView):

    def get(self,request,*args,**kwargs):

        #python_nativetype=>querry set(deserialization)

        #querry set=>python_native (serialization)

        qs=Book.objects.all()

        serializaer_instance=BookSerializer(qs,many=True)#serializer

        return Response(data=serializaer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=BookSerializer(data=request.data)#deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)
    

    
  
    
class BookRetriveUpdateDeleteView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Book.objects.get(id=id)#type=>querryset

        serializer_instance=BookSerializer(qs)#methode=serialize



        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_obj=Book.objects.get(id=id)

        serializer_instance=BookSerializer(data=request.data,instance=book_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

             return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Book.objects.get(id=id).delete()

        data={"message":"deleted"}

        return Response(data)




class BookViewSetView(viewsets.ViewSet):

    #list(),create(),update(),retrieve(),destrory()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=Book.objects.all()

        serializer_instance=BookSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwargs):

        serializer_instance=BookSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Book.objects.get(id=id)

        serializer_instance=BookSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_obj=Book.objects.get(id=id)

        serializer_instance=BookSerializer(data=request.data,instance=book_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Book.objects.get(id=id).delete()

        data={"message":"deleted"}

        return Response(data)
    

    @action(methods=["GET"],detail=False)
    def genres_list(self,request,*args,**kwargs):       #custom methode 

        genres=Book.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=genres)
    
    @action(methods=["GET"],detail=False)
    def authors_list(self,request,*args,**kwargs):

        authors=Book.objects.all().values_list("author",flat=True).distinct()

        return Response(data=authors)
    
    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        book_id=kwargs.get("pk")

        book_obj=Book.objects.get(id=book_id)

        serialiser_instance=ReviewSerializer(data=request.data)

        if serialiser_instance.is_valid():

            serialiser_instance.save(book_object=book_obj)

            return Response(data=serialiser_instance.data)
        
        else:

            return Response(data=serialiser_instance.errors)
        
class ReviewUpdateDestroyViewSet(viewsets.ViewSet):

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Review.objects.get(id=id).delete()

        data={"message":"delete"}

        return Response(data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        rev_obj=Review.objects.get(id=id)

        serialiser_instance=ReviewSerializer(data=request.data,instance=rev_obj)

        if serialiser_instance.is_valid():

            serialiser_instance.save()

            return Response(data=serialiser_instance.data)

        else:

            return Response(data=serialiser_instance.errors) 

    def retrive(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Review.objects.get(id=id)

        serialiser_instance=ReviewSerializer(qs)

        return Response(data=serialiser_instance.data)


class BookListUpdateView(generics.ListCreateAPIView):

    serializer_class=BookSerializer

    queryset=Book.objects.all()

class BookUpdateDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=BookSerializer

    queryset=Book.objects.all()

class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=ReviewSerializer

    queryset=Review.objects.all()

class ReviewCreateListView(generics.ListCreateAPIView):

    serializer_class=ReviewSerializer

    queryset=Review.objects.all()


    def perform_create(self, serializer):

        book_id=self.kwargs.get("pk")

        book_obj=Book.objects.get(id=book_id)

        serializer.save(book_object=book_obj)



        


        

    



