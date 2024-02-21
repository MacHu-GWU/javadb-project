# -*- coding: utf-8 -*-

"""
this module is generated by https://pypi.org/project/tt4human = 0.3.1
"""

from pathlib import Path
from tt4human.api import BetterStrEnum, TruthTable


class StepEnum(BetterStrEnum):
    create_virtualenv = "CREATE_VIRTUALENV"
    install_dependencies = "INSTALL_DEPENDENCIES"
    deploy_config = "DEPLOY_CONFIG"
    build_lambda_source_locally = "BUILD_LAMBDA_SOURCE_LOCALLY"
    run_code_coverage_test = "RUN_CODE_COVERAGE_TEST"
    build_documentation = "BUILD_DOCUMENTATION"
    update_documentation = "UPDATE_DOCUMENTATION"
    publish_lambda_layer = "PUBLISH_LAMBDA_LAYER"
    deploy_cdk_stack = "DEPLOY_CDK_STACK"
    run_integration_test = "RUN_INTEGRATION_TEST"
    publish_new_lambda_version = "PUBLISH_NEW_LAMBDA_VERSION"
    create_artifact_snapshot = "CREATE_ARTIFACT_SNAPSHOT"
    create_git_tag = "CREATE_GIT_TAG"
    delete_cdk_stack = "DELETE_CDK_STACK"
    delete_artifact_snapshot = "DELETE_ARTIFACT_SNAPSHOT"
    delete_config = "DELETE_CONFIG"


class SemanticBranchNameEnum(BetterStrEnum):
    main = "main"
    feature = "feature"
    fix = "fix"
    doc = "doc"
    layer = "layer"
    app = "app"
    release = "release"
    cleanup = "cleanup"


class RuntimeNameEnum(BetterStrEnum):
    local = "local"
    ci = "ci"


class EnvNameEnum(BetterStrEnum):
    devops = "devops"
    sbx = "sbx"
    tst = "tst"
    stg = "stg"
    prd = "prd"


truth_table = TruthTable.from_csv(
    path=Path(__file__).absolute().parent.joinpath("simple_lambda_truth_table.tsv"),
)

if __name__ == "__main__":
    assert truth_table.evaluate(case={'step': 'CREATE_VIRTUALENV', 'semantic_branch_name': 'main', 'runtime_name': 'local', 'env_name': 'devops'}) is True