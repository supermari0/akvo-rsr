# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from ..fields import ValidXMLCharField
from ..iso3166 import ISO_3166_COUNTRIES, CONTINENTS, COUNTRY_CONTINENTS

from akvo.codelists import models as codelist_models
from akvo.codelists.store.codelists_v201 import COUNTRY
from akvo.utils import codelist_choices, codelist_value


class Country(models.Model):
    name = ValidXMLCharField(_(u'country name'), max_length=50, unique=True, db_index=True)
    iso_code = ValidXMLCharField(
        _(u'ISO 3166 code'), max_length=2, unique=True, db_index=True, choices=ISO_3166_COUNTRIES
    )
    continent = ValidXMLCharField(_(u'continent name'), max_length=20, db_index=True)
    continent_code = ValidXMLCharField(
        _(u'continent code'), max_length=2, db_index=True, choices=CONTINENTS
    )

    def __unicode__(self):
        return self.name

    @classmethod
    def fields_from_iso_code(cls, iso_code):
        continent_code = COUNTRY_CONTINENTS[iso_code]
        name = dict(ISO_3166_COUNTRIES)[iso_code]
        continent = dict(CONTINENTS)[continent_code]
        return dict(
            iso_code=iso_code, name=name, continent=continent, continent_code=continent_code
        )

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'country')
        verbose_name_plural = _(u'countries')
        ordering = ['name']


class RecipientCountry(models.Model):
    project = models.ForeignKey(
        'Project', verbose_name=_(u'project'), related_name='recipient_countries'
    )
    country = ValidXMLCharField(_(u'country'), blank=True, max_length=2,
                                choices=codelist_choices(COUNTRY))
    percentage = models.DecimalField(
        _(u'percentage'), blank=True, null=True, max_digits=4, decimal_places=1,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    text = ValidXMLCharField(
        _(u'country description'), blank=True, max_length=50, help_text=_(u'(max 50 characters)')
    )

    def __unicode__(self):
        if self.country:
            country_unicode = self.iati_country().name
        else:
            country_unicode = u'%s' % _(u'No country specified')

        if self.percentage:
            country_unicode += u' (%s%%)' % str(self.percentage)

        return country_unicode

    def iati_country(self):
        return codelist_value(codelist_models.Country, self, 'country')

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'recipient country')
        verbose_name_plural = _(u'recipient countries')
