#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import unittest2

from testing.helpers.execution import TestSuiteLoader, TestRunner

import fab.tests.templates.config_loaders_template
from config_loaders import CustomDeploymentHostConfig, DeploymentConfigLoader

from fab.config.values.standard import DeploymentHostConfig, DeploymentHostPaths, HostAlias, RepositoryBranch


class DeploymentConfigLoaderTest(unittest2.TestCase):

    def test_can_create_partially_custom_deployment_host_configuration(self):
        """fab.tests.config.loaders.deployment_config_loader_test  Can create a partially custom deployment host configuration"""

        custom_config = DeploymentHostConfig.create_with(HostAlias.TEST, 'repository_branch', 'rsr_database_name')

        self.assertEqual(custom_config, DeploymentConfigLoader.load())

    def test_can_create_completely_custom_deployment_host_configuration(self):
        """fab.tests.config.loaders.deployment_config_loader_test  Can create a completely custom deployment host configuration"""

        custom_config = DeploymentHostConfig(RepositoryBranch.DEVELOP, 'rsrdb_develop', 'some.server.org:ssh_port',
                                             DeploymentHostPaths(CustomDeploymentHostConfig.HOST_PATHS))

        self.assertIsInstance(custom_config, DeploymentHostConfig)


def suite():
    return TestSuiteLoader().load_tests_from(DeploymentConfigLoaderTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
