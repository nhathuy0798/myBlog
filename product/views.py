from django.shortcuts import render, get_object_or_404
from .models import Product,Comment_item
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.
def post(request,pk):
    post = get_object_or_404(Product, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "product/item.html", {"post":post, "form":form})