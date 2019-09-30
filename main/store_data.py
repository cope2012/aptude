import pandas as pd
import os
from django.conf import settings
from .models import Iris


def store_data(file_path):
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    df = pd.read_csv(os.path.join(settings.BASE_DIR, file_path[1:]), header=1, names=col_names)

    if all([item in df.index for item in col_names]):
        data = [
            Iris(
                file=file_path[1:],
                sepal_length=row.sepal_length,
                sepal_width=row.sepal_width,
                petal_length=row.petal_length,
                petal_width=row.petal_width,
                species=row.species
            )
            for index, row in df.iterrows()
        ]

        try:
            Iris.objects.bulk_create(data)
        except Exception as e:
            raise Exception(e)

        return True
    else:
        raise ValueError(f'Uploaded file must has these columns: {col_names}')
