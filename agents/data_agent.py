
def process_data(df, task):
    group_by = task.get("group_by", [])
    metrics = task.get("metrics", [])

    if group_by:
        return df.groupby(group_by)[metrics].sum().reset_index()
    return df
