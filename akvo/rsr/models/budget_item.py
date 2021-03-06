# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..fields import ValidXMLCharField

from akvo.codelists.models import BudgetIdentifier, BudgetType, Currency
from akvo.codelists.store.codelists_v201 import BUDGET_IDENTIFIER,BUDGET_TYPE, CURRENCY
from akvo.utils import codelist_choices, codelist_value


class BudgetItemLabel(models.Model):
    TOTAL_BUDGET_LABEL_ID = 14
    label = ValidXMLCharField(_(u'label'), max_length=30, unique=True, db_index=True)

    def __unicode__(self):
        return self.label

    class Meta:
        app_label = 'rsr'
        ordering = ('label',)
        verbose_name = _(u'budget item label')
        verbose_name_plural = _(u'budget item labels')


class BudgetItem(models.Model):
    # DON'T translate. Need model translations for this to work
    OTHER_LABELS = [u'other 1', u'other 2', u'other 3']

    project = models.ForeignKey('Project', verbose_name=_(u'project'), related_name='budget_items')
    label = models.ForeignKey(
        BudgetItemLabel, verbose_name=_(u'project budget'), null=True,
        help_text=_(u'Select the budget item. Use the \'Other\' fields to custom budget items.')
    )
    other_extra = ValidXMLCharField(
        max_length=30, null=True, blank=True, verbose_name=_(u'"Other" labels extra info'),
        help_text=_(u'Extra information about the exact nature of an "other" budget item.'),
    )
    # Translators: This is the amount of an budget item in a currency (€ or $)
    amount = models.DecimalField(
        _(u'amount'), max_digits=14, decimal_places=2, null=True, blank=True
    )

    # Extra IATI fields
    type = ValidXMLCharField(
        _(u'budget type'), blank=True, max_length=1, choices=codelist_choices(BUDGET_TYPE),
        help_text=_(u'Select whether this is a planned or actual budget of the project.')
    )
    period_start = models.DateField(_(u'period start'), null=True, blank=True)
    period_end = models.DateField(_(u'period end'), null=True, blank=True)
    value_date = models.DateField(_(u'value date'), null=True, blank=True)
    currency = ValidXMLCharField(_(u'currency'), max_length=3, blank=True,
                                 choices=codelist_choices(CURRENCY))

    def __unicode__(self):
        if self.label:
            if self.label.label == 'Other' and self.other_extra:
                budget_unicode = self.other_extra
            else:
                budget_unicode = self.label.label
        else:
            budget_unicode = u'%s' % _(u'No budget item specified')

        if self.amount:
            budget_unicode += u' - %s %s' % (self.project.get_currency_display(),
                                             unicode('{:,}'.format(int(self.amount))))
        else:
            budget_unicode += u' - %s' % _(u'No amount specified')

        if self.type == '2':
            budget_unicode += u' %s' % _(u'(Revised)')

        return budget_unicode

    def clean(self):
        # Don't allow a start date before an end date
        if self.period_start and self.period_end and (self.period_start > self.period_end):
            raise ValidationError(
                {'period_start': u'%s' % _(u'Period start cannot be at a later time than period '
                                           u'end.'),
                 'period_end': u'%s' % _(u'Period start cannot be at a later time than period '
                                           u'end.')}
            )

    def get_label(self):
        "Needed since we have to have a vanilla __unicode__() method for the admin"
        if self.label.label in self.OTHER_LABELS:
            # display "other" if other_extra is empty.
            # Translating here without translating the other labels seems corny
            return u"other" if self.other_extra is None else self.other_extra.strip()
        else:
            return self.__unicode__()

    def iati_type(self):
        return codelist_value(BudgetType, self, 'type')

    def iati_currency(self):
        return codelist_value(Currency, self, 'currency')

    class Meta:
        app_label = 'rsr'
        ordering = ('label',)
        verbose_name = _(u'budget item')
        verbose_name_plural = _(u'budget items')


class CountryBudgetItem(models.Model):
    project = models.ForeignKey('Project', verbose_name=_(u'project'), related_name='country_budget_items')
    code = ValidXMLCharField(
        _(u'budget item'), max_length=6, blank=True, choices=codelist_choices(BUDGET_IDENTIFIER)
    )
    description = ValidXMLCharField(
        _(u'description'), max_length=100, blank=True, help_text=_(u'(max 100 characters)')
    )
    percentage = models.DecimalField(
        _(u'percentage'), blank=True, null=True, max_digits=4, decimal_places=1,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __unicode__(self):
        return self.iati_code().name if self.code else u'%s' % _(u'No code specified')

    def iati_code(self):
        return codelist_value(BudgetIdentifier, self, 'code')

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'country budget item')
        verbose_name_plural = _(u'country budget items')
