from django.urls import path
from . import views

app_name = 'menus'
urlpatterns = [
    path('<int:pk>/', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/menu_material_create/', views.MenuMaterialCreateView.as_view(), name = 'menu_material_create'),
    # path('user<int:pk>/<int:menu_id>/', views.MenuDetailView.as_view(), name = 'menu_detail'),
    # path('<int:menu_id>/', views.DetailView.as_view(), name = 'detail'),
    # path('<int:material_id>/', views.MaterialView.as_view(), name = 'material'),
    # path('<int:stock_id>/', views.StockView.as_view(), name = 'stock'),
]