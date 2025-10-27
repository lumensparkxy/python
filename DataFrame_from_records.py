import pandas as pd

def get_message_dataframe() -> pd.DataFrame:
    """
    this functions returns a dataframe containing messages 
    each json file in the messages folder corresponds to a message
    1 json file = 1 message
    """
    folder_path = "input_data/"
    import os
    import json
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), 'r') as f:
                message_data = json.load(f)
                print(f"Loaded message from {filename}: {message_data}")
                data.append(message_data)


    df = pd.DataFrame.from_records(data)
    return df

# Example usage
if __name__ == "__main__":
    df = get_message_dataframe()
    print(df.columns)  # Display the columns of the dataframe
    print(df.head())  # Display the first few rows of the dataframe
