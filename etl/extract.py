import pandas as pd


def extract_account_country():
    """Function to extract the Wealth Accounts Country data from the raw data
    folder.

    Returns:
        accounts_country: Pandas dataframe containing the Wealth Accounts
        Country data
    """
    accounts_country = pd.read_csv("data/raw/Wealth-AccountsCountry.csv")
    return accounts_country


def extract_account_data():
    """Function to extract the Wealth Accounts Data from the raw data folder.

    Returns:
        accounts_data: Pandas dataframe containing the Wealth Accounts Data
    """
    accounts_data = pd.read_csv("data/raw/Wealth-Accounts.csv")
    return accounts_data


def extract_account_series():
    """Function to extract the Wealth Accounts Series data from the raw data
    folder.

    Returns:
        accounts_series: Pandas dataframe containing the Wealth Accounts Series
        data
    """
    accounts_series = pd.read_csv("data/raw/Wealth-AccountsSeries.csv")
    return accounts_series
