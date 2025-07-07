from django.urls import path
from .import views
urlpatterns = [
    path('',views.home_view,name = "home"),
    path('sigmoid/',views.sigmoid,name="sigmoid"),
    path('predict_new/',views.predict_new,name="predictnew"),
    path('predict_view/',views.predict_view,name="predict")
]