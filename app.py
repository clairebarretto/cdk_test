#!/usr/bin/env python3

from aws_cdk import core
from infrastructure.gasfight.stack import GasFightStack
from infrastructure.hansel.stack import HanselStack
from infrastructure.hansel.lambdas.hansel_ad_third_party_resume.stack import HanselAdThirdPartyResumeStack


app = core.App()

GasFightStack(app, "gasfight-stack")
HanselStack(app, "hansel-stack")
HanselAdThirdPartyResumeStack(app, "hansel-tp-resume-stack")

app.synth()
