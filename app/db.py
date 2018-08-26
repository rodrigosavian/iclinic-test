import os

from app import util, trie


__dataset = {}


def init(app):
    global __dataset

    project_path = app.config['PROJECT_PATH']

    # populate datasets
    __dataset.update({
        'patients': trie.load_trie(
            util.csv_reader(
                os.path.join(project_path, 'patients.csv')
            )
        )
    })


def get_dataset(dataset_name):
    global __dataset
    return __dataset[dataset_name]