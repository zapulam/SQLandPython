""" Creates a single database from multiple csv files within a single folder;
    retains filename as tablename within database;
    it is best practice therefore to rename csv files to have sensable names """

import os
import sqlite3
import argparse
import pandas as pd


def create_database(args):
    dfs, file_names  = [], []
    for file in os.listdir(args.folder):
        if file.endswith(".csv"):
            dfs.append(pd.read_csv(os.path.join(args.folder, file), encoding=args.encoding))
            file_names.append(file[:-4])

    print(f'\nTable names in {args.name} - ', end='')
    for file in file_names:
        print(file)
        if i != len(file_names)-1:
            print(', ', end='')
    print('.')

    conn = sqlite3.connect(args.name)
    for i, df in enumerate(dfs):
        df.to_sql(file_names[i], conn)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, help='Path to folder with .csv files')
    parser.add_argument('--name', type=str, help='Path for database')
    parser.add_argument('--encoding', type=str, default='ISO-8859-1', help='Encoding format of csv\'s')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    if args.name[-3:] != '.db':
        raise ValueError('Database name should end in ".db"')
        exit()

    create_database(args)