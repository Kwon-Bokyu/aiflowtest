import pandas as pd

A_critera: float = 0.8
B_critera: float = 0.95


def category(x):
    if x < A_critera:
        return "A"
    elif x < B_critera:
        return "B"
    else:
        return "C"


def ABC_BY_HO(data: pd.DataFrame) -> pd.DataFrame:
    df: pd.DataFrame = pd.DataFrame(data)
    # 첫번째 전체랑 각이랑 나눈다.
    df["Percentage"] = df.iloc[:, 1] / sum(df.iloc[:, 1])
    # Percentage로 나눈다.
    df = df.sort_values(by="Percentage", ascending=False)
    # 각 당 합쳐간다.
    df["comulative"] = df["Percentage"].cumsum()
    # A,B,C 인지 지정해준다.
    df["Category"] = df["comulative"].map(category)
    return df


def productmix(product_nm, sales, revenue) -> pd.DataFrame:
    store: pd.DataFrame = pd.DataFrame(
        {"product_nm": product_nm, "sales": sales, "revenue": revenue}
    )
    store["sales_mix"] = store["sales"] / sum(store["sales"])
    store = store.sort_values(by="sales", ascending=False)
    store["comulative_sales"] = store["sales_mix"].cumsum()
    store = store.sort_values(by="revenue", ascending=False)
    store["revenue_mix"] = store["revenue"] / sum(store["revenue"])
    store["comulative_revenue"] = store["revenue_mix"].cumsum()
    store["sales_category"] = store["comulative_sales"].map(category)
    store["revenue_category"] = store["comulative_revenue"].map(category)
    store["product_mix"] = store["sales_category"] + "_" + store["revenue_category"]
    return store
