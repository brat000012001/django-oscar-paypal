from oscar.apps.checkout.apps import CheckoutConfig
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig


class PayPalConfig(OscarConfig):
    name='apps'
    verbose_name=_('Paypal Checkout')
    namespace="apps"

