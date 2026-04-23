def validate_from_config(df, config):
    results = []

    for column, rules in config["columns"].items():

        if rules.get("not_null"):
            result = df[column].isnull().sum() == 0
            results.append(result)

        if rules.get("unique"):
            result = df[column].duplicated().sum() == 0
            results.append(result)

    return all(results)