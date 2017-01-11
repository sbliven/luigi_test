"""
Example of parameter interpolation within a config file.

In luigi.cfg, refer to other variables with single curly braces

run with:

> PYTHONPATH="." luigi --module formattedconfig MyTask --local-scheduler

See https://groups.google.com/forum/#!searchin/luigi-user/interpolate$20parameter%7Csort:relevance/luigi-user/KyJMaZQcqks/ZlLPc-f8MQAJ
"""

import luigi
from luigi.parameter import Parameter,DateHourParameter

class FormattedConfig(luigi.Config):
    eppoc = DateHourParameter()
    workdir = Parameter()

    def __getattribute__(self,name):
        # Any string attributes (e.g. Parameters) get passed through format
        # This expands singly-bracketed variables
        value = super(FormattedConfig, self).__getattribute__(name)
        if hasattr(value, "format"):
            newvalue = value.format(**self.__dict__)
            while newvalue != value:
                value = newvalue
                newvalue = value.format(**self.__dict__)
        return value

    def get(self,key,default=None):
        # Make the config dict-like for use with handlebars
        try:
            return getattr(self,key)
        except AttributeError:
            return default

config = FormattedConfig()
class MyTask(luigi.Task):
    def run(self):
        print("WORKDIR=%s"% config.workdir )

if __name__ == "__main__":
    luigi.run()
