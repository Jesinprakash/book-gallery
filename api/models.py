from django.db import models

class Book(models.Model):

    title=models.CharField(max_length=200)

    author=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    price=models.FloatField()

    genre=models.CharField(max_length=200)
    

    @property
    def review(self):

        return Review.objects.filter(book_object=self)
    
    @property
    def review_count(self):

        return self.review.count()
    
    @property
    def avg_rating(self):

        avg=0
        review=self.review

        if review:

            avg=sum([r.rating for r in review])/self.review_count

        return avg


    

    
    

    def __str__(self) -> str:
        return self.title
    
from django.core.validators import MinValueValidator,MaxValueValidator  
class Review(models.Model):

    book_object=models.ForeignKey(Book,on_delete=models.CASCADE)

    comment=models.CharField(max_length=200)

    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    user=models.CharField(max_length=100)
