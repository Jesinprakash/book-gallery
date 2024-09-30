from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("v1/books",views.BookViewSetView,basename="books")

router.register("v1/reviews",views.ReviewUpdateDestroyViewSet,basename="reviews")


urlpatterns = [

    path('books/',views.BookCreateListView.as_view()),

    path('books/<int:pk>/',views.BookRetriveUpdateDeleteView.as_view()),

    path('v2/books/',views.BookListUpdateView.as_view()),

    path('v2/books/<int:pk>/',views.BookUpdateDeleteDetailView.as_view()),

    path('v2/reviews/<int:pk>/',views.ReviewUpdateDeleteView.as_view()),

    path('v2/book/<int:pk>/review/add/',views.ReviewCreateListView.as_view())



    
]+router.urls