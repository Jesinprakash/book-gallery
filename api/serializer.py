from rest_framework import serializers  #serializer is used for convert python native to querryset and quarrey to python python native

from api.models import Book,Review



class ReviewSerializer(serializers.ModelSerializer):

    book_object=serializers.StringRelatedField()
    
    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=["id","book_object"]


class BookSerializer(serializers.ModelSerializer):

    # review=ReviewSerializer(read_only=True,many=True)

    review=ReviewSerializer(read_only=True,many=True)

    # review_count=serializers.CharField(read_only=True)

    review_count=serializers.SerializerMethodField(read_only=True)

    # avg_rating=serializers.IntegerField(read_only=True)

    avg_rating=serializers.IntegerField(read_only=True)

    class Meta:

        model=Book

        fields=["id","title","author","language","price","genre","review","review_count","avg_rating"]            #__all__ takes entire elements in the model 


    def get_review_count(self,obj):

        return Review.objects.filter(book_object=obj).count()

    def get_avg_rating(self,obj):

        review=Review.objects.filter(book_object=obj)

        avg=0

        if review:

            avg=sum([r.rating for r in review])/review.count()

        return avg
    
    def get_review(self,obj):

        qs=Review.objects.filter(book_object=obj)

        serialiser_instance=ReviewSerializer(qs,many=True)

        return serialiser_instance.data
    
   