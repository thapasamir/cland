from django.urls import path
from .import views
urlpatterns = [
	path('',views.HomeView.as_view(),name='home'),
	path('cateogry',views.CateogryView.as_view(),name='cateogry'),
	path('view/<int:pk>/', views.HomeDetail.as_view(), name='homedetail'),
	path('view/<int:pk>/comment/', views.AddComment.as_view(), name='addcomment'),
	path('cateogry/<int:id>/',views.DetailCatView,name='detail'),
	path('Createcontent', views.CreateContent.as_view(), name='Create'),
	path('Createcateogry', views.CreateCateogry.as_view(), name='CreateCateo'),
	path('accounts/signup', views.SignUpView.as_view(), name='Signup'),

]