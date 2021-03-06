# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from rest_framework import serializers

from akvo.rsr.models import Partnership

from .rsr_serializer import BaseRSRSerializer


class PartnershipSerializer(BaseRSRSerializer):

    partner_type = serializers.Field(source='iati_role_to_partner_type')

    class Meta:
        model = Partnership
