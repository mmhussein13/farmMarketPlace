// Add to cart functionality with AJAX
$(document).ready(function() {
    // Quantity increment/decrement in product detail
    $('.quantity-right-plus').click(function(e) {
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
        $('#quantity').val(quantity + 1);
    });

    $('.quantity-left-minus').click(function(e) {
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
        if (quantity > 1) {
            $('#quantity').val(quantity - 1);
        }
    });

    // Payment processing
    $('#payment-form').submit(function(e) {
        e.preventDefault();
        
        // Here would normally be payment gateway integration code
        // For now, simulate a successful payment
        
        let orderData = {
            orderID: $('#order_number').val(),
            transID: 'TRANS_' + Math.floor(Math.random() * 1000000),
            payment_method: $('input[name="payment_method"]:checked').val(),
            status: 'COMPLETED'
        };
        
        $.ajax({
            url: '/payments/',
            method: 'POST',
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            data: JSON.stringify(orderData),
            contentType: 'application/json',
            success: function(response) {
                window.location.href = '/order_complete?order_number=' + response.order_number + '&payment_id=' + response.transID;
            },
            error: function(error) {
                console.log('Error processing payment:', error);
                alert('There was a problem processing your payment. Please try again.');
            }
        });
    });

    // Handle product search form submission
    $('#search-form').submit(function(e) {
        if ($('#search-input').val().trim() === '') {
            e.preventDefault();
        }
    });
});
