"""This module defines the Payment class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class Payment:
    """
    Payment Class
    
    Purpose:
        Processes bill payments by using a specific payment strategy.
        Demonstrates the strategy pattern.
    """

    def __init__(self, strategy):
        """
        Purpose:
            Initialises the payment objectwith the given strategy.
            
        Args:
            strategy (PaymentStrategy): The selected strategy of payment.
            
        Raises:
            ValueError: If the strategy is invalid.
        """
        if isinstance(strategy, PaymentStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Invalid Strategy")
        
    def pay_bill(self, billing_account, payee, amount):
        """
        Method: pay_bill
        
        Purpose:
            Proceses the assigned payment strategy.
            
        Args:
            billing_account: The BillingAccount object.
            payee: The payee being paid.
            amount: The amount of payment.
            
        Returns:
            str: Message returned by the applied strategy.
        """
        return self.strategy.process_payment(billing_account, payee, amount)
