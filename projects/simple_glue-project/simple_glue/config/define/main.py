# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

from ...vendor.import_agent import aws_ops_alpha
from ..._api import EnvNameEnum, detect_current_env

# You may have a long list of config field definition
# put them in different module and use Mixin class
from .app import AppMixin
from .glue_deploy import GlueDeployMixin
from .glue_job import GlueJob, GlueJobMixin


# inherit order matters, typically, you want to use your own Mixin class
# to override the default behavior, so you should inherit aws_ops_alpha.Env
# at the end. You can find more details about MRO at https://www.python.org/download/releases/2.3/mro/
@dataclasses.dataclass
class Env(
    AppMixin,
    GlueDeployMixin,
    GlueJobMixin,
    aws_ops_alpha.BaseEnv,
):
    @classmethod
    def from_dict(cls, data: dict):
        data["glue_jobs"] = {
            name: GlueJob(
                short_name=name,
                **dct,
            )
            for name, dct in data.get("glue_jobs", {}).items()
        }
        env = cls(**data)
        for glue_job in env.glue_jobs.values():
            glue_job.env = env
        return env


@dataclasses.dataclass
class Config(aws_ops_alpha.BaseConfig[Env]):
    @classmethod
    def get_current_env(cls) -> str:  # pragma: no cover
        return detect_current_env()

    @cached_property
    def sbx(self):  # pragma: no cover
        return self.get_env(env_name=EnvNameEnum.sbx.value)

    @cached_property
    def tst(self) -> Env:  # pragma: no cover
        return self.get_env(env_name=EnvNameEnum.tst.value)

    @cached_property
    def prd(self) -> Env:  # pragma: no cover
        return self.get_env(env_name=EnvNameEnum.prd.value)

    @cached_property
    def env(self) -> Env:
        return self.get_env(env_name=self.get_current_env())
