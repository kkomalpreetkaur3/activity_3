"""This module defines the PenaltyStrategy class."""

__author__ = "komalpreet Kaur"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    """Applies a $10 penalty for incomplete payments."""

    def process_payment(self, billing_account, payee, amount):

        billing_account.deduct_balance(payee, amount)
        balance = billing_account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            billing_account.add_balance(payee, 10.00)
            new_balance = billing_account.get_balance(payee)
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${new_balance:.2f}."
