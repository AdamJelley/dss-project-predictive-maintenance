# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
assets_at_risk = dataiku.Dataset("Assets_at_risk")
assets_at_risk_df = assets_at_risk.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

assets_at_risk_py_df = assets_at_risk_df # For this sample code, simply copy input to output


# Write recipe outputs
assets_at_risk_py = dataiku.Dataset("Assets_at_risk_py")
assets_at_risk_py.write_with_schema(assets_at_risk_py_df)
