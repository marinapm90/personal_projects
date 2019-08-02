import pandas as pd


def new_column(df, col1, col2):
    df["new_column"] = df[col1]-df[col2]
    return df

def category(df,col):
    kickstarter_category = df[col].value_counts()
    return kickstarter_category

def types(df, col1, col2, col3):
    kickstarter_types = df.groupby(by=["col1"]).agg({"col2": ['sum'], "col3": ["sum"]})
    return kickstarter_types

def country(df, col):
    kickstarter_country = df[col].value_counts()[0:10]
    return kickstarter_country

def star( df, col1, col2):
    kickstarter_start = df.groupby(by=col1).agg({col2: ['count']})
    return kickstarter_start

def end (df, col1, col2):
    kickstarter_end = df.groupby(by=col1).agg({col2: ['count']})
    return kickstarter_end

def success (df, col1, col2):
    kickstarter_success = df.groupby(by=[col1]).agg({col2 : ['count']})
    return kickstarter_success




