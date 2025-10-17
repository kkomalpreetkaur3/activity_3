"""This module defines the PaymentStrategy class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    PaymentStrategy Class
    
    Purpose:
        Abstract superclass that defines the required method for all payment 
        strategy subclasses.
    """

    @abstractmethod
    def process_payment(self, billing_account, payee, amount):
        """
        Abstract Method: process_payment
        
        Purpose:
            Defines a method that all concrete strategies must implement.
            
        Args:
            billing_account: The BillingAccount object.
            payee: The payee to which the payment applies.
            amount: The payment amount.
        """
        pass 