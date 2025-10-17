"""This module defines the PenaltyStrategy class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from .payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    """
    PenaltyStrategy Class
    
    Purpose:
       Applies penalty of $10.00 when the balance is not fully paid.
    """

    def process_payment(self, billing_account, payee, amount):
        """
        Method: process_payment
        
        Purpose:
            Deducts payment amount and adds penalty if the payment does not
            clear the full balance.
            
        Args: 
            billing_account: The BillingAccount instance.
            payee: The payee being paid.
            amount: The payment amount.
            
        Returns:
            str: With confirmation message after applying payment or prnalty.
        """
        billing_account.deduct_balance(payee, amount)
        balance = billing_account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            billing_account.add_balance(payee, 10.00)
            new_balance = billing_account.get_balance(payee)
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${new_balance:.2f}."
