import sqlite3
import requests
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import sys
print(sys.path)


class FredApi:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.api_key_fred = self.config["api"]["key"]
        self.endpoint = self.config["api"]["endpoint"]

    def _load_config(self, file_path: str) -> dict:
        # Load YAML configuration file and return as dictionary
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    
    # Make API request and call Preprocess
    def fetch_and_preprocess_series(self, series_id: str) -> pd.DataFrame:
        url = f"{self.endpoint}/series/observations?series_id={series_id}&api_key={self.api_key_fred}&file_type=json"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            observations = response.json()["observations"]
            df = pd.DataFrame(observations)
            return self._preprocess(df)
        except requests.RequestException as e:
            print(f"Failed to retrieve data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame
        
    # Preprocess DataFrame: remove rows with '.' in 'value', drop unnecessary columns, convert 'date' column to datetime
    def _preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        if not df.empty:
            df = df[~df['value'].str.contains('^\.$', na=False)]
            df = df.drop(["realtime_start", "realtime_end"], axis=1)
            df["date"] = pd.to_datetime(df["date"])
            df["value"] = pd.to_numeric(df["value"])
        return pd.DataFrame(df)


class DataBase:
    
    @staticmethod
    def create_table(database: str, name_table: str):
        # Parameters to database URL
        params_dic = {
            "host": "localhost",
            "database": f"../../data/raw/{database}.db"
        }
        try:
            connection = sqlite3.connect(f"{params_dic['database']}")
            cursor = connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} (date TEXT PRIMARY KEY, value FLOAT);")
            cursor.close()
            connection.close()
            print(f"Table: {name_table} was created with success.")
        except (RuntimeError, TypeError, NameError, ValueError, KeyboardInterrupt) as err:
            print(err)
            pass
    
    @staticmethod
    def delete_table(database: str, name_table: str):
        params_dic = {
            "host": "localhost",
            "database": f"../../data/raw/{database}.db"
        }
            
        try:
            connection = sqlite3.connect(f"{params_dic['database']}")
            cursor = connection.cursor()

            # Drop the table if it exists
            cursor.execute(f"DROP TABLE IF EXISTS {name_table};")

            connection.commit()
            print(f"Table '{name_table}' deleted successfully.")
        except sqlite3.Error as error:
            print("Failed to delete table:", error)
        finally:
            if connection:
                connection.close()        
    
    @staticmethod
    def insert_data(database: str, name_table: str, df: pd.DataFrame):
        params_dic = {
            "host": "localhost",
            "database": f"../../data/raw/{database}.db"
        }

        try:
            connection = sqlite3.connect(f"{params_dic['database']}")
            cursor = connection.cursor()
            for index, row in df.iterrows():
                try:
                    # Extract date and value from DataFrame row
                    date = str(row["date"].strftime("%Y-%m-%d"))
                    value = row["value"]
                    print(date, value)
                    cursor.execute(f"INSERT INTO {name_table} (date, value) VALUES (?, ?);", (date, value))
                except sqlite3.IntegrityError as e:
                    print(f"Skipping insertion for date {index} {date} due to UNIQUE constraint violation: {e}")
                    connection.rollback()  # Rollback the transaction
                    continue
            connection.commit()
            print("Data insertion successful.")
        except ValueError as e:
            print("Error:", e)

        except sqlite3.IntegrityError as e:
            print(f"Skipping insertion for date{index} {date} due to UNIQUE constraint violation: {e}")
            connection.rollback()  # Rollback the transaction
            
        except sqlite3.Error as e:
            print("Error:", e)
            
        finally:
            if connection:
                connection.close()



if __name__ == "__main__":
    api_client = FredApi(config_path="../../config.yaml")
    
    #df_sp500 = api_client.fetch_and_preprocess_series(series_id="sp500")
    #print(df_sp500)
    #data_sp500 = DataBase()
    #data_sp500.create_table(database="sp500", name_table="series")
    #data_sp500.delete_table(database="sp500", name_table="series")
    #data_sp500.insert_data(database="sp500", name_table="series", df=df)

    df_unemployment = api_client.fetch_and_preprocess_series(series_id="unrate")
    print(df_unemployment)
    data_unemployment = DataBase()
    #data_unemployment.create_table(database="unrate", name_table="series")
    #data_unemployment.delete_table(database="unrate", name_table="series")
    data_unemployment.insert_data(database="unrate", name_table="series", df=df_unemployment)
    