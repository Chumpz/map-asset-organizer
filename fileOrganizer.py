import os
import shutil


asset_prefixes = {
    'SM_': 'Meshes',
    'SK_': 'Animation',
    'A_': 'Animation',
    'T_': 'Textures',
    'ABC_': 'Alembic'
}


def organize(directory='', *args):
    print(directory)
    list_of_file = os.listdir(directory)
    print(list_of_file)

    for file in list_of_file:
        for prefix in asset_prefixes:
            if file.startswith(prefix):
                final_map = asset_prefixes[prefix]
                print(final_map+'---success---')
                if os.path.exists(directory+'/'+final_map):
                    shutil.move(directory+'/'+file, directory+'/'+final_map+'/'+file)
                else:
                    os.makedirs(directory + '/' + final_map)
                    shutil.move(directory+'/'+file, directory+'/'+final_map+'/'+file)
                break


if __name__ == "__main__":
    print(tuple(asset_prefixes))
