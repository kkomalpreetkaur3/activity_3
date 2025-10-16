"""This module defines the PartialPaymentStrategy class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy

class PartialPaymentStrategy(PaymentStrategy):
    """Process partial payments without penalty."""

    def process_payment(self, billing_account, payee, amount):
        
        billing_account.deduct_balance(payee, amount)
        balance = billing_account.get_balance(payee)

        """Checks balance status and return message."""
        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
        
