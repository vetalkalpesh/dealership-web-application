from django.urls import path
from . import views

urlpatterns = [
    path("dealers/", views.dealers_list, name="dealers"),
    path("dealers/state/<str:state>/", views.dealers_by_state, name="dealers_by_state"),
    path("dealers/<int:dealer_id>/", views.dealer_detail, name="dealer_detail"),
    path("dealers/<int:dealer_id>/reviews/", views.dealer_reviews, name="dealer_reviews"),
    path("dealers/<int:dealer_id>/reviews/create/", views.create_review, name="create_review"),
    path("carmakes/", views.car_makes, name="car_makes"),
    path("analyze/", views.analyze_review, name="analyze_review"),
]
