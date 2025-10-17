"""This module defines the PartialPaymentStrategy class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy

class PartialPaymentStrategy(PaymentStrategy):
    """
    PartialPaymentStrategy Class
   
    Purpose:
       Allows partial payments to be processed without penalty.
    """

    def process_payment(self, billing_account, payee, amount):
        """
        Method: process_payment
        
        Purpose:
            Processes a partial payment for the given payee.
            
        Args:
            billing_account: The BillingAccount instance.
            payee: The payee whose bill is being paid.
            amount: The amount being paid.
        
        Returns:
            str: Confirmation message after payment is processed."""
        billing_account.deduct_balance(payee, amount)
        balance = billing_account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
        
