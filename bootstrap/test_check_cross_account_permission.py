# -*- coding: utf-8 -*-

"""
This script test the cross account IAM permission in GitHub Action using OIDC.
It is used in GitHub action only, it won't work on local machine because it cannot
assume the GitHub Action OIDC principal.
"""

import os
from boto_session_manager import BotoSesManager
from cross_aws_account_iam_role.api import (
    IamRoleArn,
    print_account_info,
)
from run_bootstrap import (
    sbx_res_name,
    tst_res_name,
    prd_res_name,
)

print("the devops (CI/CD) IAM entity:")

bsm = BotoSesManager()
print_account_info(bsm)

aws_region = "us-east-1"
workload_aws_account_id_and_role_name_list = [
    (os.environ["SBX_AWS_ACCOUNT_ID"], sbx_res_name),
    (os.environ["TST_AWS_ACCOUNT_ID"], tst_res_name),
    (os.environ["PRD_AWS_ACCOUNT_ID"], prd_res_name),
]
for aws_account_id, role_name in workload_aws_account_id_and_role_name_list:
    bsm_assume_role = bsm.assume_role(
        role_arn=IamRoleArn(
            account=aws_account_id,
            name=role_name,
        ).arn,
        duration_seconds=900,
    )
    print_account_info(bsm_assume_role)
