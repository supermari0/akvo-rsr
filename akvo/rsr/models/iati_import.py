# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .iati_project_import import IatiProjectImport


def file_path(self, filename):
    return 'db/iati_import/%s' % filename


class IatiImport(models.Model):
    PENDING_STATUS = 1
    RETRIEVING_STATUS = 2
    IN_PROGRESS_STATUS = 3
    COMPLETED_STATUS = 4
    CANCELLED_STATUS = 5

    STATUS_CODES = (
        (PENDING_STATUS, _(u'pending')),
        (RETRIEVING_STATUS, _(u'retrieving file')),
        (IN_PROGRESS_STATUS, _(u'import in progress')),
        (COMPLETED_STATUS, _(u'completed')),
        (CANCELLED_STATUS, _(u'cancelled'))
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_(u'user'), related_name='iati_imports'
    )
    url = models.URLField(_(u'url'), blank=True)
    local_file = models.FileField(_(u'local file'), blank=True, upload_to=file_path)
    status = models.PositiveSmallIntegerField(_(u'status'), choices=STATUS_CODES,
                                              default=PENDING_STATUS)
    start_date = models.DateTimeField(_(u'start date'), null=True, blank=True)
    end_date = models.DateTimeField(_(u'end date'), null=True, blank=True)
    projects = models.ManyToManyField(
        'Project', verbose_name=_(u'projects'), through=IatiProjectImport, blank=True
    )

    def __unicode__(self):
        if self.url:
            return u'%s: %s (%s)' % (_(u'IATI import'),
                                     self.url,
                                     self.show_status())
        elif self.local_file:
            return u'%s: %s (%s)' % (_(u'IATI import'),
                                     str(self.local_file).rsplit('/',1)[1],
                                     self.show_status())
        else:
            return u'%s: %s' % (_(u'IATI import'),
                                _(u'no file'))

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'IATI import')
        verbose_name_plural = _(u'IATI imports')

    def show_status(self):
        return dict(map(lambda x: x, self.STATUS_CODES))[self.status]
