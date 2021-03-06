# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from ..fields import ValidXMLCharField

from akvo.codelists import models as codelist_models
from akvo.codelists.store.codelists_v201 import SECTOR_VOCABULARY
from akvo.utils import codelist_choices, codelist_value


class Sector(models.Model):
    project = models.ForeignKey('Project', verbose_name=_(u'project'), related_name='sectors')
    sector_code = ValidXMLCharField(
        _(u'sector code'), blank=True, max_length=5,
        help_text=_(u'Enter the sector code of the sectors that the project is working within.<br>'
                    u'See these lists for the DAC-5 and DAC-3 sector codes:<br>'
                    u'- <a href="http://iatistandard.org/201/codelists/Sector/" target="_blank">'
                    u'DAC-5 sector codes</a><br>'
                    u'- <a href="http://iatistandard.org/201/codelists/SectorCategory/" '
                    u'target="_blank">DAC-3 sector codes</a>')
    )
    text = ValidXMLCharField(
        _(u'description'), blank=True, max_length=100, help_text=_(u'(max 100 characters)')
    )
    vocabulary = ValidXMLCharField(
        _(u'vocabulary'), blank=True, max_length=5, choices=codelist_choices(SECTOR_VOCABULARY)
    )
    percentage = models.DecimalField(
        _(u'sector percentage'), blank=True, null=True, max_digits=4, decimal_places=1,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_(u'You can set the percentage of the project that is relevant for '
                    u'this sector here.')
    )

    def __unicode__(self):
        if self.sector_code:
            try:
                sector_unicode = self.iati_sector().name.capitalize()
            except Exception as e:
                sector_unicode = u'%s' % _(u'Sector code not found')
        else:
            sector_unicode = u'%s' % _(u'No sector code specified')

        if self.percentage:
            sector_unicode += u' (%s%%)' % str(self.percentage)

        return sector_unicode


    def iati_sector_codes(self):
        if self.sector_code and (self.vocabulary == '1' or self.vocabulary == 'DAC'):
            return self.sector_code, codelist_value(codelist_models.Sector, self, 'sector_code')
        elif self.sector_code and (self.vocabulary == '2' or self.vocabulary == 'DAC-3'):
            return self.sector_code, codelist_value(codelist_models.SectorCategory,
                                                    self,
                                                    'sector_code')
        else:
            return self.sector_code, self.sector_code

    def iati_sector(self):
        if self.sector_code and (self.vocabulary == '1' or self.vocabulary == 'DAC'):
            return codelist_value(codelist_models.Sector, self, 'sector_code')
        elif self.sector_code and (self.vocabulary == '2' or self.vocabulary == 'DAC-3'):
            return codelist_value(codelist_models.SectorCategory, self, 'sector_code')
        else:
            return self.sector_code

    def iati_vocabulary(self):
        return codelist_value(codelist_models.SectorVocabulary, self, 'vocabulary')

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'sector')
        verbose_name_plural = _(u'sectors')
        ordering = ['sector_code', ]
