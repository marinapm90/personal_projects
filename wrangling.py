import pandas as pd


def new_column(df, col1, col2):
    df["new_column"] = df[col1]-df[col2]
    return df


def category(df, col):
    data = df[col].value_counts()
    return data


def types(df, col1, col2, col3):
    data = df.groupby(by=[col1]).agg({col2: ['sum'], col3: ["sum"]})
    return data


def country(df, col):
    data = df[col].value_counts()[0:10]
    return data


def star(df, col1, col2):
    data = df.groupby(by=col1).agg({col2: ['count']})
    return data


def end(df, col1, col2):
    data = df.groupby(by=col1).agg({col2: ['count']})
    return data


def success(df, col1, col2):
    data = df.groupby(by=[col1]).agg({col2: ['count']})
    return data





