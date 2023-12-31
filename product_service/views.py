# Standard Library Imports
import logging

# Django Core Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local App Imports
from admin_dashboard.views import AdminRequiredMixin
from user_dashboard.views import BuyerRequiredMixin
from .forms import AdminProductCreationForm, AdminServiceCreationForm
from .models import (Product, Service, Category,
                     ServiceType, CodeType, Download, SCOPE_TYPE)
from homepage.models import STATUS
from .validate_file import validate_image_size
from checkout.models import Order, OrderLineItem, ORDER_STATUS

logger = logging.getLogger(__name__)

# ADMIN CREATE Product & Service

# Product Creation instance


@method_decorator(login_required, name='dispatch')
class AdminProductCreation(AdminRequiredMixin, View):
    """Create product instances for the marketplace """
    template_name = 'admin-dashboard/create_product.html'

    def get(self, request, *args, **kwargs):
        form = AdminProductCreationForm(initial={'author': request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AdminProductCreationForm(request.POST, request.FILES)

        # Validating Image KB
        image = request.FILES.get('image')
        if image:
            max_upload_size = 500000
            if image.size > max_upload_size:
                form.add_error('image',
                               "File size must not exceed 500KB.")

        if form.is_valid():
            product_instance = form.save(commit=False)
            product_instance.author = request.user
            product_instance.save()
            form.save_m2m()
            messages.success(
                request,
                "Congratulations! The product instance has been created!")
            return redirect('admin_all_products')
        else:
            return render(
                request, self.template_name,
                {'form': form})

# READ Product instances


@method_decorator(login_required, name='dispatch')
class ProductBaseListView(AdminRequiredMixin, ListView):
    """ Base view for listing Product instances."""
    model = Product

    def get_queryset(self):
        """ Return product instances ordered by creation date."""
        return Product.objects.order_by('-created_on')


@method_decorator(login_required, name='dispatch')
class ProductList(ProductBaseListView):
    """ Read all created product instances tempalte"""
    template_name = 'admin-dashboard/all_products.html'
    context_object_name = 'admin_all_products'


# UPDATE Product instance

@method_decorator(login_required, name='dispatch')
class BaseUpdateProductView(AdminRequiredMixin, View):
    """Base class for product list view."""
    template_name = None

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug)
        return render(request, self.template_name, context)

    def get_context_data(self, slug):
        categories = Category.objects.all()
        services = ServiceType.objects.all()
        codes = CodeType.objects.all()

        queryset = Product.objects.order_by('-created_on')
        product = get_object_or_404(queryset, slug=slug)

        # Dynamically filter choices for
        # download_url based on the current instance
        related_downloads = Download.objects.filter(product=product)

        status = STATUS
        scope = SCOPE_TYPE
        offer_code = product.code.all()
        offer_service = product.service.all()
        files_selected = product.download_url.all()

        return {
            "categories": categories,
            "services": services,
            "codes": codes,

            "product": product,
            "status": status,
            "scope": scope,
            "offer_code": offer_code,
            "offer_service": offer_service,
            "related_downloads": related_downloads,
            "files_selected": files_selected,
            "user_authenticated": self.request.user.is_authenticated
        }


@method_decorator(login_required, name='dispatch')
class AdminUpdateProductView(BaseUpdateProductView):
    """View to update product instance"""
    template_name = 'admin-dashboard/update_product.html'

    def post(self, request, slug, *args, **kwargs):

        product = get_object_or_404(Product, slug=slug)

        product.title = request.POST.get('title')
        product.sku = request.POST.get('sku')
        product.price = request.POST.get('price')

        product.category = Category.objects.get(
            pk=request.POST.get('category'))

        status = request.POST.get('status')
        product.status = int(status)

        type = request.POST.get('type')
        product.type = int(type)

        code = request.POST.getlist('code')
        product.code.set(code)

        services = request.POST.getlist('service')
        product.service.set(services)

        product.preview = request.POST.get('preview')

        product.docs = request.POST.get('docs')

        description = request.POST.get('description')
        product.description = description[:528]

        product.excerpt = request.POST.get('excerpt')

        image = request.FILES.get(
            'image')
        if image and validate_image_size(request, image):
            product.image = image

        product.image_url = request.POST.get('image_url')

        related_downloads = request.POST.getlist('related_downloads')
        product.download_url.set(related_downloads)

        product.save()

        messages.success(
            request, "Congratulations! The product instance has been updated!")
        return redirect('admin_product_update', slug=product.slug)

# DELETE Product instance


@method_decorator(login_required, name='dispatch')
class ProductDelete(AdminRequiredMixin, DeleteView):
    """View for deleting product instances."""
    model = Product
    template_name = None
    allowed_roles = [1]

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.status == 2:
            messages.error(
                request, "Error: product's status must be suspended or draft.")
            return redirect('admin_all_products')

        if self.request.user.role not in self.allowed_roles:
            messages.error(
                request, "Error: User does not have the required role")
            return redirect('admin_all_products')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)

    def get_success_url(self):
        messages.success(self.request, 'Product Instance has been deleted!')
        return reverse_lazy('admin_all_products')


# CREATE Service instance

@method_decorator(login_required, name='dispatch')
class AdminServiceCreation(AdminRequiredMixin, View):
    """Create service instances for the marketplace """
    template_name = 'admin-dashboard/create_service.html'

    def get(self, request, *args, **kwargs):
        form = AdminServiceCreationForm(initial={'author': request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AdminServiceCreationForm(request.POST, request.FILES)

        # Validating Image KB
        image = request.FILES.get('image')
        if image:
            max_upload_size = 500000
            if image.size > max_upload_size:
                form.add_error('image',
                               "File size must not exceed 500KB.")

        if form.is_valid():
            service_instance = form.save(commit=False)
            service_instance.author = request.user
            service_instance.save()
            form.save_m2m()
            messages.success(
                request,
                "Congratulations! The service instance has been created!")
            return redirect('admin_all_services')
        else:
            return render(
                request, self.template_name,
                {'form': form})

# READ Service instances


@method_decorator(login_required, name='dispatch')
class ServiceBaseListView(AdminRequiredMixin, ListView):
    """ Base view for listing Service instances."""
    model = Service

    def get_queryset(self):
        """ Return service instances ordered by creation date."""
        return Service.objects.order_by('-created_on')


@method_decorator(login_required, name='dispatch')
class ServiceList(ServiceBaseListView):
    """ Read all created service instances tempalte"""
    template_name = 'admin-dashboard/all_services.html'
    context_object_name = 'admin_all_services'

# UPDATE Service instance


@method_decorator(login_required, name='dispatch')
class BaseUpdateServiceView(AdminRequiredMixin, View):
    """Base class for service list view."""
    template_name = None

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug)
        return render(request, self.template_name, context)

    def get_context_data(self, slug):

        categories = Category.objects.all()
        services = ServiceType.objects.all()
        codes = CodeType.objects.all()

        queryset = Service.objects.order_by('-created_on')
        service = get_object_or_404(queryset, slug=slug)

        # Dynamically filter choices for
        # download_url based on the current instance
        related_downloads = Download.objects.filter(service=service)

        status = STATUS
        scope = SCOPE_TYPE
        offer_code = service.code.all()
        offer_service = service.service.all()
        files_selected = service.download_url.all()

        return {
            "categories": categories,
            "services": services,
            "codes": codes,

            "service": service,
            "status": status,
            "scope": scope,
            "offer_code": offer_code,
            "offer_service": offer_service,
            "related_downloads": related_downloads,
            "files_selected": files_selected,
            "user_authenticated": self.request.user.is_authenticated
        }


@method_decorator(login_required, name='dispatch')
class AdminUpdateServiceView(BaseUpdateServiceView):
    """View to update service instance"""
    template_name = 'admin-dashboard/update_service.html'

    def post(self, request, slug, *args, **kwargs):

        service = get_object_or_404(Service, slug=slug)

        service.title = request.POST.get('title')
        service.sku = request.POST.get('sku')
        service.price = request.POST.get('price')

        service.category = Category.objects.get(
            pk=request.POST.get('category'))

        status = request.POST.get('status')
        service.status = int(status)

        type = request.POST.get('type')
        service.type = int(type)

        code = request.POST.getlist('code')
        service.code.set(code)

        services = request.POST.getlist('service')
        service.service.set(services)

        service.preview = request.POST.get('preview')

        service.docs = request.POST.get('docs')

        description = request.POST.get('description')
        service.description = description[:528]

        service.excerpt = request.POST.get('excerpt')

        image = request.FILES.get(
            'image')
        if image and validate_image_size(request, image):
            service.image = image

        service.image_url = request.POST.get('image_url')

        related_downloads = request.POST.getlist('related_downloads')
        service.download_url.set(related_downloads)

        service.save()

        messages.success(
            request, "Congratulations! The service instance has been updated!")
        return redirect('admin_service_update', slug=service.slug)

# DELETE Service instance


@method_decorator(login_required, name='dispatch')
class ServiceDelete(AdminRequiredMixin, DeleteView):
    """View for deleting service instances."""
    model = Service
    template_name = None
    allowed_roles = [1]

    def dispatch(self, request, *args, **kwargs):
        service = self.get_object()
        if service.status == 2:
            messages.error(
                request, "Error: service's status must be suspended or draft.")
            return redirect('admin_all_services')

        if self.request.user.role not in self.allowed_roles:
            messages.error(
                request, "Error: User does not have the required role")
            return redirect('admin_all_services')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Service, slug=slug)

    def get_success_url(self):
        messages.success(self.request, 'Service Instance has been deleted!')
        return reverse_lazy('admin_all_services')

# BAG view


class ShoppingCartView(ListView):
    model = Product
    template_name = 'bag/bag.html'

# Order Management

# READ Order ListView


@method_decorator(login_required, name='dispatch')
class AdminOrderListView(AdminRequiredMixin, ListView):
    """ListView for admin/global orders. Another approach instead of View"""
    model = Order
    template_name = 'admin-dashboard/all_orders.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        try:

            queryset = Order.objects.annotate(
                ordercount=Count('id')).order_by('-date')
            queryset = queryset.prefetch_related(
                Prefetch('lineitems',
                         queryset=OrderLineItem.objects.select_related(
                             'product', 'service'))
            )
            return queryset
        except Exception as e:
            logger.error(f"Error fetching Order instances: {str(e)}")
            messages.error(self.request, 'Error fetching Order instances.')
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_orders = context[self.context_object_name]

        context['all_orders'] = all_orders
        return context


@method_decorator(login_required, name='dispatch')
class BuyerOrderListView(BuyerRequiredMixin, ListView):
    """ListView for user order instances. Another approach instead of View"""
    model = Order
    template_name = 'user-dashboard/all_orders.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        try:
            user = self.request.user
            queryset = Order.objects.filter(buyer_profile=user).annotate(
                ordercount=Count('id')).order_by('-date')

            queryset = queryset.prefetch_related(
                Prefetch('lineitems',
                         queryset=OrderLineItem.objects.select_related(
                             'product', 'service'))
            )
            return queryset
        except Exception as e:
            logger.error(f"Error fetching Order instances: {str(e)}")
            messages.error(self.request, 'Error fetching Order instances.')
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_orders = context[self.context_object_name]

        context['all_orders'] = all_orders
        return context

# UPDATE Order ListView


@method_decorator(login_required, name='dispatch')
class AdminBaseUpdateOrderView(AdminRequiredMixin, View):
    """Base class for service list view."""
    template_name = None

    def get(self, request, order_number, *args, **kwargs):
        context = self.get_context_data(order_number)
        return render(request, self.template_name, context)

    def get_context_data(self, order_number):
        queryset = Order.objects.order_by('-date')
        order = get_object_or_404(queryset, order_number=order_number)
        status = ORDER_STATUS
        return {
            "order": order,
            "status": status,
            "user_authenticated": self.request.user.is_authenticated
        }


@method_decorator(login_required, name='dispatch')
class AdminUpdateOrderView(AdminBaseUpdateOrderView):
    """View to update service instance"""
    template_name = 'admin-dashboard/update_order.html'

    def post(self, request, order_number, *args, **kwargs):
        order = get_object_or_404(Order, order_number=order_number)

        status = request.POST.get('status')
        order.status = int(status)
        order.save()

        messages.success(
            request, "Congratulations! The order instance has been updated!")
        return redirect('all_orders_admin')


@method_decorator(login_required, name='dispatch')
class UserBaseUpdateOrderView(BuyerRequiredMixin, View):
    """Base class for service list view."""
    template_name = None

    def get(self, request, order_number, *args, **kwargs):
        context = self.get_context_data(order_number)
        return render(request, self.template_name, context)

    def get_context_data(self, order_number):
        queryset = Order.objects.order_by('-date')
        order = get_object_or_404(queryset, order_number=order_number)
        return {
            "order": order,
            "user_authenticated": self.request.user.is_authenticated
        }


@method_decorator(login_required, name='dispatch')
class UserUpdateOrderView(UserBaseUpdateOrderView):
    """View to update service instance"""
    template_name = 'user-dashboard/update_order.html'

    def post(self, request, order_number, *args, **kwargs):
        order = get_object_or_404(Order, order_number=order_number)

        email = request.POST.get('email')
        if email != request.user.email:
            messages.error(request, 'Please, use your own email!')
        else:
            order.email = email
            order.save()
            messages.success(
                request, "Congratulations! The order has been updated!")
        return redirect('all_orders_user')
