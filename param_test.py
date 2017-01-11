""" Test code for checking parameter override rules

Results:
- Use hyphens in cli params and underscores in code and config files
- Changes to [ParamTestBase] or --ParamTestBase-base-param are ignored

To run, override params in luigi.cfg and/or on the CLI with either hyphens or underscores

> PYTHONPATH="." luigi --module param_test ParamTest --local-scheduler --ParamTestBase-base-param="CLI BASE"
"""
import logging
import luigi

class ParamTestBase(luigi.Task):
    base_param = luigi.Parameter(default="default value for base_param")

class ParamTest(ParamTestBase):
    underscore_param = luigi.Parameter(default="default value for underscore_param")
    hyphen_param = luigi.Parameter(default="default value for hyphen_param")
    def run(self):
        print("base_param = %s" % self.base_param)
        print("underscore_param = %s" % self.underscore_param)
        print("hyphen_param = %s" % self.hyphen_param)
