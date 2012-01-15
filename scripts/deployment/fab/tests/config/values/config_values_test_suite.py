#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.tests.config.values.ci_deployment_config_test import CIDeploymentConfigTest
from fab.tests.config.values.custom_deployment_config_test import CustomDeploymentConfigTest
from fab.tests.config.values.custom_user_credentials_test import CustomUserCredentialsTest
from fab.tests.config.values.data_host_paths_test import DataHostPathsTest
from fab.tests.config.values.deployment_host_paths_test import DeploymentHostPathsTest
from fab.tests.config.values.host_path_values_test import HostPathValuesTest
from fab.tests.config.values.ssh_connection_values_test import SSHConnectionValuesTest
from fab.tests.config.values.user_credentials_test import UserCredentialsTest


def config_values_suite():
    return TestSuiteLoader().create_suite_from_classes([CIDeploymentConfigTest, CustomDeploymentConfigTest, CustomUserCredentialsTest,
                                                        DataHostPathsTest, DeploymentHostPathsTest, HostPathValuesTest,
                                                        SSHConnectionValuesTest, UserCredentialsTest])

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(config_values_suite())
