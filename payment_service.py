import stripe

def process_payment(amount, currency="usd", payment_method=None):
    # Updated to PaymentIntent API in Stripe v2022-11-15
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method=payment_method,
        confirm=True,
        description="Order Payment"
    )
