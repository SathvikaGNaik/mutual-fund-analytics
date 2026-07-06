"""
Interactive SQL Analytics Runner
Author: Sathvika G Naik
"""

import sqlite3
import pandas as pd

from scripts.utils.config import DATABASE
from scripts.utils.helpers import print_header


QUERIES = {

    "1": {
        "title": "Funds by Fund House",
        "query": """
            SELECT
                fund_house,
                COUNT(*) AS total_funds
            FROM fund_master
            GROUP BY fund_house
            ORDER BY total_funds DESC;
        """
    },

    "2": {
        "title": "Top 10 Five-Year Returns",
        "query": """
            SELECT
                scheme_name,
                fund_house,
                return_5yr_pct
            FROM scheme_performance
            ORDER BY return_5yr_pct DESC
            LIMIT 10;
        """
    },

    "3": {
        "title": "Lowest Expense Ratio",
        "query": """
            SELECT
                scheme_name,
                fund_house,
                expense_ratio_pct
            FROM scheme_performance
            ORDER BY expense_ratio_pct ASC
            LIMIT 10;
        """
    },

    "4": {
        "title": "Average Return by Category",
        "query": """
            SELECT
                category,
                ROUND(AVG(return_5yr_pct),2) AS average_return
            FROM scheme_performance
            GROUP BY category
            ORDER BY average_return DESC;
        """
    },

    "5": {
        "title": "Average Return by Risk Grade",
        "query": """
            SELECT
                risk_grade,
                ROUND(AVG(return_5yr_pct),2) AS average_return
            FROM scheme_performance
            GROUP BY risk_grade
            ORDER BY average_return DESC;
        """
    },

    "6": {
        "title": "Transaction Type Distribution",
        "query": """
            SELECT
                transaction_type,
                COUNT(*) AS total_transactions
            FROM investor_transactions
            GROUP BY transaction_type;
        """
    },

    "7": {
        "title": "Top States by Investment",
        "query": """
            SELECT
                state,
                ROUND(SUM(amount_inr),2) AS total_investment
            FROM investor_transactions
            GROUP BY state
            ORDER BY total_investment DESC
            LIMIT 10;
        """
    },

    "8": {
        "title": "Payment Mode Distribution",
        "query": """
            SELECT
                payment_mode,
                COUNT(*) AS total_transactions
            FROM investor_transactions
            GROUP BY payment_mode
            ORDER BY total_transactions DESC;
        """
    },

    "9": {
        "title": "Average Investment by City Tier",
        "query": """
            SELECT
                city_tier,
                ROUND(AVG(amount_inr),2) AS average_investment
            FROM investor_transactions
            GROUP BY city_tier;
        """
    },

    "10": {
        "title": "Average Investment by Age Group",
        "query": """
            SELECT
                age_group,
                ROUND(AVG(amount_inr),2) AS average_investment
            FROM investor_transactions
            GROUP BY age_group
            ORDER BY average_investment DESC;
        """
    },

    "11": {
        "title": "Top 10 Funds by AUM",
        "query": """
            SELECT
                scheme_name,
                fund_house,
                aum_crore
            FROM scheme_performance
            ORDER BY aum_crore DESC
            LIMIT 10;
        """
    },

    "12": {
        "title": "Average Expense Ratio by Fund House",
        "query": """
            SELECT
                fund_house,
                ROUND(AVG(expense_ratio_pct),2) AS average_expense
            FROM scheme_performance
            GROUP BY fund_house
            ORDER BY average_expense ASC;
        """
    },

    "13": {
        "title": "Highest Sharpe Ratio Funds",
        "query": """
            SELECT
                scheme_name,
                sharpe_ratio
            FROM scheme_performance
            ORDER BY sharpe_ratio DESC
            LIMIT 10;
        """
    },

    "14": {
        "title": "Highest Alpha Funds",
        "query": """
            SELECT
                scheme_name,
                alpha
            FROM scheme_performance
            ORDER BY alpha DESC
            LIMIT 10;
        """
    },

    "15": {
        "title": "Highest Volatility Funds",
        "query": """
            SELECT
                scheme_name,
                std_dev_ann_pct
            FROM scheme_performance
            ORDER BY std_dev_ann_pct DESC
            LIMIT 10;
        """
    }

}


def execute_query(sql, title):

    print_header(title)

    conn = sqlite3.connect(DATABASE)

    try:

        df = pd.read_sql_query(sql, conn)

        print(df)

        print(f"\nRows Returned: {len(df)}")

    except Exception as e:

        print(f"\nError:\n{e}")

    finally:

        conn.close()


def show_menu():

    print_header("SQL ANALYTICS")

    for key in QUERIES:
        print(f"{key}. {QUERIES[key]['title']}")

    print("\n16. Custom SQL Query")

    print("0. Exit")


def main():

    while True:

        show_menu()

        choice = input("\nEnter choice: ").strip()

        if choice == "0":

            print("\nGoodbye!")

            break

        elif choice == "16":

            print("\nEnter SQL Query:")
            sql = input("> ")

            execute_query(sql, "Custom SQL")

        elif choice in QUERIES:

            execute_query(
                QUERIES[choice]["query"],
                QUERIES[choice]["title"]
            )

        else:

            print("\nInvalid choice.\n")


if __name__ == "__main__":
    main()