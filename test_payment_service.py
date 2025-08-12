import stripe
from payment_service import process_payment

def test_process_payment(monkeypatch):
    # Mock Stripe API
    def mock_create(**kwargs):
        return {"status": "succeeded", **kwargs}

    monkeypatch.setattr(stripe.PaymentIntent, "create", mock_create)

    result = process_payment(5000, "usd", "pm_card_visa")
    assert result["status"] == "succeeded"
    assert result["amount"] == 5000
