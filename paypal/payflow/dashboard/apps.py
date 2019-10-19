from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from oscar.core.application import OscarDashboardConfig
from django.utils.translation import gettext_lazy as _


class PayFlowDashboardConfig(OscarDashboardConfig):

    label = 'paypal_payflow_dashboard'
    name = 'paypal.payflow.dashboard'
    namespace = 'paypal_payflow_dashboard'
    verbose_name = _('PayPal Payflow Dashboard')

    default_permissions = ['is_staff', ]

    def ready(self):
        from paypal.payflow.dashboard import views
        self.list_view = views.TransactionListView
        self.detail_view = views.TransactionDetailView

    def get_urls(self):
        urlpatterns = [
            url(r'^transactions/$', self.list_view.as_view(),
                name='paypal-payflow-list'),
            url(r'^transactions/(?P<pk>\d+)/$', self.detail_view.as_view(),
                name='paypal-payflow-detail'),
        ]
        return self.post_process_urls(urlpatterns)
