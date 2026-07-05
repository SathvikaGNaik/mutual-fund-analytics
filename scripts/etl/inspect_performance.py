from scripts.utils.config import RAW_DATA
from scripts.utils.helpers import load_csv, print_header

def main():
    print_header("SCHEME PERFORMANCE")

    df = load_csv(RAW_DATA / "07_scheme_performance.csv")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()