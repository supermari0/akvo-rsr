# -*- coding: utf-8 -*-

"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the
Akvo RSR module. For additional details on the GNU license please
see < http://www.gnu.org/licenses/agpl.html >.
"""


from .benchmark import BenchmarkViewSet
from .benchmark_name import BenchmarknameViewSet
from .budget_item import BudgetItemViewSet, CountryBudgetItemViewSet
from .budget_item_label import BudgetItemLabelViewSet
from .category import CategoryViewSet
from .country import CountryViewSet
from .custom_field import OrganisationCustomFieldViewSet, ProjectCustomFieldViewSet
from .employment import EmploymentViewSet, approve_employment, set_group
from .focus_area import FocusAreaViewSet
from .goal import GoalViewSet
from .indicator import IndicatorViewSet, IndicatorPeriodViewSet
from .internal_organisation_id import InternalOrganisationIDViewSet
from .invoice import InvoiceViewSet
from .keyword import KeywordViewSet
from .legacy_data import LegacyDataViewSet
from .link import LinkViewSet
from .organisation import OrganisationViewSet
from .organisation_location import OrganisationLocationViewSet, MapOrganisationLocationViewSet
from .partner_site import PartnerSiteViewSet
from .partnership import PartnershipViewSet
from .planned_disbursement import PlannedDisbursementViewSet
from .policy_marker import PolicyMarkerViewSet
from .project import ProjectViewSet, ProjectExtraViewSet, ProjectUpViewSet
from .project_editor import (project_editor_delete_document,
                             project_editor_delete_photo,
                             project_editor_import_results,
                             project_editor_remove_keyword,
                             project_editor_step1,
                             project_editor_step2,
                             project_editor_step3,
                             project_editor_step4,
                             project_editor_step5,
                             project_editor_step6,
                             project_editor_step7,
                             project_editor_step8,
                             project_editor_step9,
                             project_editor_step10,
                             project_editor_organisation_logo)
from .project_comment import ProjectCommentViewSet
from .project_document import ProjectDocumentViewSet
from .project_condition import ProjectConditionViewSet
from .project_contact import ProjectContactViewSet
from .project_iati_checks import ProjectIatiCheckView
from .project_location import (ProjectLocationViewSet,
                               AdministrativeLocationViewSet,
                               MapProjectLocationViewSet)
from .project_update import (ProjectUpdateViewSet,
                             ProjectUpdateExtraViewSet,
                             upload_indicator_update_photo)
from .project_update_location import ProjectUpdateLocationViewSet, MapProjectUpdateLocationViewSet
from .publishing_status import PublishingStatusViewSet
from .recipient_country import RecipientCountryViewSet
from .related_project import RelatedProjectViewSet
from .region import RecipientRegionViewSet
from .result import ResultViewSet
from .sector import SectorViewSet
from .server_info import server_info
from .transaction import TransactionViewSet, TransactionSectorViewSet
from .typeahead import (typeahead_country,
                        typeahead_organisation,
                        typeahead_project,
                        typeahead_projectupdate)
from .user import (UserViewSet, change_password, update_details,
                   request_organisation)

__all__ = [
    'AdministrativeLocationViewSet',
    'approve_employment',
    'BenchmarknameViewSet',
    'BenchmarkViewSet',
    'BudgetItemLabelViewSet',
    'BudgetItemViewSet',
    'CategoryViewSet',
    'change_password',
    'CountryViewSet',
    'CountryBudgetItemViewSet',
    'EmploymentViewSet',
    'FocusAreaViewSet',
    'GoalViewSet',
    'IndicatorPeriodViewSet',
    'IndicatorViewSet',
    'InternalOrganisationIDViewSet',
    'InvoiceViewSet',
    'KeywordViewSet',
    'LegacyDataViewSet',
    'LinkViewSet',
    'MapOrganisationLocationViewSet',
    'MapProjectLocationViewSet',
    'MapProjectUpdateLocationViewSet',
    'OrganisationViewSet',
    'OrganisationLocationViewSet',
    'OrganisationCustomFieldViewSet',
    'PartnershipViewSet',
    'PartnerSiteViewSet',
    'PlannedDisbursementViewSet',
    'PolicyMarkerViewSet',
    'ProjectCommentViewSet',
    'ProjectConditionViewSet',
    'ProjectContactViewSet',
    'ProjectCustomFieldViewSet',
    'ProjectDocumentViewSet',
    'ProjectExtraViewSet',
    'ProjectIatiCheckView',
    'ProjectLocationViewSet',
    'ProjectUpdateExtraViewSet',
    'ProjectUpdateLocationViewSet',
    'ProjectUpdateViewSet',
    'ProjectUpViewSet',
    'ProjectViewSet',
    'project_editor_delete_document',
    'project_editor_delete_photo',
    'project_editor_import_results',
    'project_editor_step1',
    'project_editor_step2',
    'project_editor_step3',
    'project_editor_step4',
    'project_editor_step5',
    'project_editor_step6',
    'project_editor_step7',
    'project_editor_step8',
    'project_editor_step9',
    'project_editor_step10',
    'project_editor_organisation_logo',
    'PublishingStatusViewSet',
    'RecipientCountryViewSet',
    'RecipientRegionViewSet',
    'RelatedProjectViewSet',
    'request_organisation',
    'ResultViewSet',
    'SectorViewSet',
    'server_info',
    'set_group',
    'TransactionViewSet',
    'TransactionSectorViewSet',
    'typeahead_country',
    'typeahead_organisation',
    'typeahead_project',
    'typeahead_projectupdate',
    'update_details',
    'upload_indicator_update_photo',
    'UserViewSet',
]
