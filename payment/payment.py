"""This module defines the Payment class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class Payment:
    """Applies a selected payment strategy to process payments."""

    def __init__(self, strategy):
        
        if isinstance(strategy, PaymentStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Invalid Strategy")
        
    def pay_bill(self, billing_account, payee, amount):
        """Use the strategy to process a bill payment."""
        return self.strategy.process_payment(billing_account, payee, amount)
