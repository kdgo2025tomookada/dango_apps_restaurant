from django.shortcuts import render
from django.urls import reverse_lazy
import requests
import urllib
from django.views import generic#便利なテンプレート機能を使えるようにする
from .models import Category,Shop

class DetailView(generic.DetailView):
    # ↓ 使用するテンプレートファイルを指定
    template_name = 'gourmet_guide/wonderful_shop_detail.html'
    model = Shop
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_instance = self.get_object()
        address = shop_instance.address
        makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
        s_quote = urllib.parse.quote(address)
        response = requests.get(makeUrl + s_quote)
        print("response", response)
        coordinates = response.json()[0]["geometry"]["coordinates"]
        print("coordinates", coordinates)
        reversed_coordinates = reversed(coordinates)
        context['coordinates'] = ",".join(map(str, reversed_coordinates))
        print("context['coordinates']", context['coordinates'])
        return context


    





class IndexViews(generic.ListView):#データが一覧表示されるようにする
    model = Shop#どのモデルを一覧表示するか
class CreateView(generic.edit.CreateView):
    model = Shop
    fields = "__all__"
class UpdateView(generic.edit.UpdateView):
    model = Shop
    fields = "__all__"

class DeleteView(generic.edit.DeleteView):
    model = Shop
    # reverse_lazyの引数に表示したいページのnameを指定
    success_url = reverse_lazy('gourmet_guide:index')