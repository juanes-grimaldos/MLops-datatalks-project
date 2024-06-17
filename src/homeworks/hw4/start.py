import pickle
import pandas as pd
import sys
import numpy as np
import requests
import pandas as pd
from io import BytesIO

categorical = ['PULocationID', 'DOLocationID']


def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we raise an exception for bad responses
    return BytesIO(response.content)

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    # Assume `categorical` is defined elsewhere in your script
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

# URL of the Parquet file
year = int(sys.argv[1])
month = int(sys.argv[2])
url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet'


def apply_model(output_file):
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    file_content = download_file(url)
    df = read_data(file_content)
    
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    
    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred


    
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )
    # mean duration
    f = df_result['predicted_duration'].mean()
    print(f)



if __name__ == '__main__':
    apply_model('predictions_q5.parquet')
