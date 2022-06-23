"""
stripe_dashboard.py

Creates a simple dashboard to display data from Stripe
"""
import stripe

from deephaven import empty_table
from deephaven.plot.figure import Figure
from deephaven.time import millis_to_datetime

import os

stripe.api_key = os.environ['STRIPE_API_KEY']

def date_time_converter(charge):
    return millis_to_datetime(charge["created"] * 1000)

def amount_converter(charge):
    return charge["amount"]

charges = stripe.Charge.list(limit=100)["data"]

result = empty_table(len(charges)).update("Charges = charges[i]")
result = result.update(["DateTime = (DateTime)date_time_converter(Charges)", "Amount = (int)amount_converter(Charges)"])

charges_over_time = Figure().plot_xy(series_name="ChargesOverTime", t=result, x="DateTime", y="Amount").show()
