from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from admin_portal.products.forms import AddAuthorForm, AddBookForm, AddPublisherForm, UpdatePublisherForm
from product.models import  Author, Book, Publisher
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


### Product add with Ajax ##################
class Add_Book_Ajax(LoginRequiredMixin,CreateView):
    model = Book
    from_class = AddBookForm
    fields = ['author_name', 'book_description', 'publisher_name','book_name', 'book_price', 'book_image', ]
    success_url = reverse_lazy('products:add_book_ajax')
    template_name = "admin_temp/book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.all()

        context['book_data'] = book
        return context

    def form_valid(self, form):
        messages.success(self.request, f"Your Product has been Added succesfully")
        return super().form_valid(form)



class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['author_name','book_description','publisher_name', 'book_name', 'book_price', 'book_image', ]
    template_name = "admin_temp/book_update.html"
    success_url = reverse_lazy('products:book_product_ajax')

    def form_valid(self, form):
        messages.success(self.request, f"Your Product has been Updated succesfully")
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin,DeleteView):
    def get(self, request, pk):
        user = request.user
        book = Book.objects.get(pk=self.kwargs['pk'])
        if book:
            book.delete()
            messages.success(
                request, 'Your Product has been Deleted succesfully!')
        return redirect('products:add_book_ajax')

### This part is any product delete sure option in other page html

    # model = Product
    # template_name = "admin_temp/book_delete.html"
    # success_url = reverse_lazy('products:product_list')

    # def form_valid(self, form):
    #     messages.warning(self.request,f"Your Product Delete  succesfully")
    #     return super().form_valid(form)


@login_required
def publisher_list(request):
    publisher_form = AddPublisherForm()
    update_form = UpdatePublisherForm()
    publishers = Publisher.objects.all()
    return render(request, 'admin_temp/publisher_list.html', {"publisher_form": publisher_form, 'update_form': update_form, "publishers": publishers})


def add_publisher(request):
    if request.method == "POST":
        publisher_form = AddPublisherForm(request.POST)
        if publisher_form.is_valid():
            instance = publisher_form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": publisher_form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)


        
class PublisherUpdateView(LoginRequiredMixin,UpdateView):
    model = Publisher
    fields = ['publisher_name', ]
    template_name = "admin_temp/publisher_update.html"
    success_url = reverse_lazy('products:publisher_list')

    def form_valid(self, form):
        messages.success(self.request, f"Your Publisher has been Update succesfully")
        return super().form_valid(form)


class PublisherDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        publisher = Publisher.objects.get(pk=self.kwargs['pk'])
        if publisher:
            publisher.delete()
            messages.success(self.request, f'Publisher has been deleted!')
        return redirect('products:publisher_list')

############## AUTHER ####################


class Add_Auther_Ajax(LoginRequiredMixin,CreateView):
    model = Author
    from_class = AddAuthorForm
    fields = ['author_name', ]
    success_url = reverse_lazy('products:author_list')
    template_name = "admin_temp/author_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.all()
        context['author_data'] = author
        return context

    def form_valid(self, form):
        messages.success(self.request, f"Your Auther has been Added succesfully")
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin,UpdateView):
    model = Author
    fields = ['author_name', ]
    template_name = "admin_temp/author_update.html"
    success_url = reverse_lazy('products:author_list')

    def form_valid(self, form):
        messages.success(self.request, f"Your Author has been Update succesfully")
        return super().form_valid(form)


class AuthorDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        auther = Author.objects.get(pk=self.kwargs['pk'])
        if auther:
            auther.delete()
            messages.success(self.request, f'Auther has been deleted!')
        return redirect('products:author_list')
