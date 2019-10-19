from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from oscar.core.application import OscarDashboardConfig
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_class


class ExpressDashboardConfig(OscarDashboardConfig):
    label = 'paypal_express_dashboard'
    name = 'paypal.express.dashboard'
    namespace = 'paypal_express_dashboard' 
    verbose_name = _('Paypal Express Dashboard')

    default_permissions = ['is_staff', ]

    def ready(self):
        from paypal.express.dashboard import views
        self.list_view = views.TransactionListView
        self.detail_view = views.TransactionDetailView

    def get_urls(self):
        urlpatterns = [
            url(r'^transactions/$', self.list_view.as_view(),
                name='paypal-express-list'),
            url(r'^transactions/(?P<pk>\d+)/$', self.detail_view.as_view(),
                name='paypal-express-detail'),
        ]
        return self.post_process_urls(urlpatterns)
