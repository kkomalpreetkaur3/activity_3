"""This module defines the PaymentStrategy class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """Abstract superclass for all payment strategies."""

    @abstractmethod
    def process_payment(self, billing_account, payee, amount):
        """All concrete strategies must implement this method."""
        pass 