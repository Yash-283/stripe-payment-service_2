import stripe

def process_payment(amount, currency="usd", payment_method=None):
    # Deprecated method - needs to be updated
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        source=payment_method,
        description="Order Payment"
    )
