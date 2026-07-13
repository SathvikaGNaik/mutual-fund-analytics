
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR / "data" / "processed" / "performance_metrics.csv"
)

print("\nAvailable Risk Grades:")

print(performance["risk_grade"].unique())

risk = input("\nEnter Risk Appetite: ")

recommend = (

    performance[
        performance["risk_grade"]
        .str.lower()
        ==
        risk.lower()
    ]

    .sort_values(
        "Sharpe_Ratio",
        ascending=False
    )

    .head(3)

)

print(
    recommend[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "Sharpe_Ratio",
            "Fund_Score"
        ]
    ]
)