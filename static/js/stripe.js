$(function() {
    $("#payment-form").submit(function() {
        
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val(),
            address_line1: $("#id_address1").val(),
            address_line2: $("#id_address2").val(),
            address_city: $("#id_town_or_city").val(),
            address_country: $("#id_country").val(),
            address_zip: $("#id_postcode").val(),
            name: $("#id_full_name").val()
        };
        $("#submit_payment_btn").attr("disabled", true);
        Stripe.createToken(card, function(status, response) {
            if (status === 200) {
                $("#credit-card-errors").hide();
                $("#id_stripe_id").val(response.id);
    
                // Prevent the Credit card Details from being submitted to our server
                $("#id_credit_card_number").removeAttr('name');
                $("#id_expiry_month").removeAttr('name');
                $("#id_expiry_year").removeAttr('name');
                $("#id_cvv").removeAttr('name');
    
                form.submit();
                    
            } else {
                $("#stripe-error-message").text(response.error.message);
                $("#credit-card-errors").show();
                $("#submit_payment_btn").attr("disabled", false);
            }
        });
        return false;
    });
});