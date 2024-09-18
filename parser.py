import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Input start directory ')
    args = parser.parse_args()
    return args.path


def list_files(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent+'Имя файла - ', f + ' размер - ' + str(os.path.getsize(root+"\\"+f))+"b"))


if __name__ == '__main__':
    path = create_parser()
    list_files(path)
