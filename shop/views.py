from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from shop.models import Item
import logging
import re
from .forms import ItemForm
from django.views.generic import CreateView, UpdateView

logger = logging.getLogger(__name__)

# def post_list(request):
#     logger.error('Somthing went wrong!')

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    logger.debug('query: {}'.format(q))
    return render(request, 'shop/item_list.html', {
        'item_list':qs,
        'q':q,
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

# def item_new(request, item=None):
#     error_list = []
#     initial = {}

#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item) 
#         if form.is_valid():
#             item = form.save()
#             return redirect(item)
#     else:
#         form = ItemForm(instance=item)
#     #     data = request.POST
#     #     files = request.FILES

#     #     name = data.get('name')
#     #     desc = data.get('desc')
#     #     price = data.get('price')
#     #     photo = files.get('photo')
#     #     is_publish = data.get('is_publish') in (True, 't', 'True', '1')

#     #     # 유효성 검사
#     #     if len(name) < 2:
#     #         error_list.append('name을 2글자 이상 입력해주세요.')

#     #     if re.match(r'^[\da-zA-Z\s]+$', desc):
#     #         error_list.append('한글을 입력해주세요.')

#     #     if not error_list:
#     #         # 저장 시도
#     #         if item is None:
#     #             item = Item()

#     #         item.name = name
#     #         item.desc = desc
#     #         item.price = price
#     #         item.is_publish = is_publish

#     #         if photo:
#     #             item.photo.save(photo.name, photo, save=False)

#     #         try:
#     #             item.save()
#     #         except Exception as e:
#     #             error_list.append(e)
#     #         else:
#     #             return redirect(item)

#     #     initial = {
#     #         'name': name,
#     #         'desc': desc,
#     #         'price': price,
#     #         'photo': photo,
#     #         'is_publish': is_publish,
#     #     }
#     # else:
#     #     if item is not None:
#     #         initial = {
#     #             'name': item.name,
#     #             'desc': item.desc,
#     #             'price': item.price,
#     #             'photo': item.photo,
#     #             'is_publish': item.is_publish,
#     #         }
#     return render(request, 'shop/item_form.html',{
#         'form':form,
#     })
#     # return render(request, 'shop/item_form.html', {
#     #     'error_list': error_list,
#     #     'initial': initial,
#     # })


# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)