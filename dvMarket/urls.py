"""dvMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from dvMarket.settings import MEDAI_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'categorys', CategoryViewSet, base_name="categorys")

goods_list = GoodsListViewSet.as_view({
    "get" : "list",  # 将get请求绑定到list方法
})


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),  # 后台
    url(r'^api-auth/', include('rest_framework.urls')),  # DRF的登录和注销
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDAI_ROOT}),  # 图片
    url(r'docs/', include_docs_urls(title="dvMarkt_cb")),  # 生成DRF文档

    url(r'^', include(router.urls)),
    url(r'^login/', views.obtain_auth_token),  # token，会返回一个唯一的token值
]
