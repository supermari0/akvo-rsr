#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os, unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

CUSTOM_CONFIG_VALUES_TEMPLATE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../../config/values/custom.py.template'))
imp.load_source('custom_config_values', CUSTOM_CONFIG_VALUES_TEMPLATE_PATH)

from custom_config_values import CustomDeploymentConfig

from fab.config.values.standard import DeploymentHostPaths, RepositoryBranch


class CustomDeploymentConfigTest(unittest2.TestCase):

    def test_can_create_custom_deployment_configuration(self):
        """fab.tests.config.values.custom_deployment_config_test  Can create custom deployment configuration"""

        custom_config = CustomDeploymentConfig(RepositoryBranch.DEVELOP, 'rsrdb_develop', 'some.server.org:ssh_port',
                                               DeploymentHostPaths(CustomDeploymentConfig.HOST_PATHS))

        self.assertEqual(custom_config, CustomDeploymentConfig.create())


def suite():
    return TestSuiteLoader().load_tests_from(CustomDeploymentConfigTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
