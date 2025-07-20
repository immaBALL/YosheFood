from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order, OrderItem, Contact
from decimal import Decimal

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')
        
        # Basic validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
        else:
            try:
                # Create and save contact message
                Contact.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
    
    # GET request or after POST - show the page
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def order(request):
    if request.method == 'POST':
        # Handle form submission - redirect to review instead of creating order
        import json
        
        # Get selected products from form
        selected_products_json = request.POST.get('selected_products', '[]')
        selected_products = json.loads(selected_products_json)
        
        if not selected_products:
            messages.error(request, 'Please select at least one product.')
            return redirect('order')
        
        # Store selected products in session for review
        request.session['selected_products'] = selected_products_json
        request.session['total_amount'] = request.POST.get('total_amount', '0')
        
        # Redirect to review page
        return redirect('order_review')
    
    # GET request - show the order form
    products = Product.objects.all()
    
    # Pass customer details from session to template
    context = {
        'products': products,
        'customer_name': request.session.get('customer_name', ''),
        'customer_email': request.session.get('customer_email', ''),
        'guest_checkout': request.session.get('guest_checkout', False)
    }
    
    return render(request, 'order.html', context)

def order_review(request):
    # Check if we have the necessary session data
    selected_products_json = request.session.get('selected_products')
    if not selected_products_json:
        messages.error(request, 'No order data found. Please start over.')
        return redirect('customer_details')
    
    if request.method == 'POST':
        # Handle order confirmation
        action = request.POST.get('action')
        if action == 'confirm':
            return redirect('confirm_order')
    
    # GET request - show review page
    import json
    selected_products = json.loads(selected_products_json)
    
    # Prepare order items for display
    order_items = []
    total_amount = 0
    
    for item_data in selected_products:
        try:
            product = Product.objects.get(id=item_data['product_id'])
            quantity = int(item_data['quantity'])
            price = Decimal(str(product.price))
            total_price = price * quantity
            
            order_items.append({
                'product': product,
                'quantity': quantity,
                'price': price,
                'total_price': total_price
            })
            
            total_amount += total_price
        except Product.DoesNotExist:
            messages.error(request, f'Product with ID {item_data["product_id"]} not found.')
            return redirect('order')
    
    context = {
        'order_items': order_items,
        'total_amount': total_amount,
        'customer_name': request.session.get('customer_name', ''),
        'customer_email': request.session.get('customer_email', ''),
        'guest_checkout': request.session.get('guest_checkout', False)
    }
    
    return render(request, 'order_review.html', context)

def confirm_order(request):
    # Check if we have the necessary session data
    selected_products_json = request.session.get('selected_products')
    if not selected_products_json:
        messages.error(request, 'No order data found. Please start over.')
        return redirect('customer_details')
    
    # Get customer details from session
    customer_name = request.session.get('customer_name', '')
    customer_email = request.session.get('customer_email', '')
    is_guest_order = request.session.get('guest_checkout', False)
    
    # Get selected products from session
    import json
    selected_products = json.loads(selected_products_json)
    
    try:
        # Create the order
        order = Order.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            is_guest_order=is_guest_order
        )
        
        total_price = 0
        
        # Create order items for each selected product
        for item_data in selected_products:
            product = Product.objects.get(id=item_data['product_id'])
            quantity = int(item_data['quantity'])
            price = Decimal(str(product.price))
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
            
            total_price += price * quantity
        
        messages.success(request, f'Order #{order.id} placed successfully! Total: ${total_price}')
        
        # Clear session data after successful order
        if 'customer_name' in request.session:
            del request.session['customer_name']
        if 'customer_email' in request.session:
            del request.session['customer_email']
        if 'guest_checkout' in request.session:
            del request.session['guest_checkout']
        if 'selected_products' in request.session:
            del request.session['selected_products']
        if 'total_amount' in request.session:
            del request.session['total_amount']
            
        return redirect('order_confirmation', order_id=order.id)
        
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
        return redirect('order')
    except ValueError:
        messages.error(request, 'Invalid quantity.')
        return redirect('order')

def customer_details(request):
    if request.method == 'POST':
        # Store customer details in session for use in order page
        request.session['customer_name'] = request.POST.get('customer_name')
        request.session['customer_email'] = request.POST.get('customer_email')
        request.session['guest_checkout'] = request.POST.get('guest_checkout') == 'on'
        
        # Redirect to order page
        return redirect('order')
    
    return render(request, 'customer_details.html')

def order_confirmation(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order_items = order.items.all()
        total_amount = sum(item.total_price for item in order_items)
        
        context = {
            'order': order,
            'order_items': order_items,
            'total_amount': total_amount,
        }
        return render(request, 'order_confirmation.html', context)
    except Order.DoesNotExist:
        messages.error(request, 'Order not found.')
        return redirect('index')