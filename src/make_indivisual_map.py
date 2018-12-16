# -*- coding: utf-8 -*-
# make_indivisual_map.py
# make one-window map from "map_all.csv"
# you need to delete 1st row's 0,...,0 when running game@makeMap

import pandas as pd

CHIP_NUM_COL = 26 # const chipNumCol: int :: 25 {WinWidth/chipWidth}

def main():
    map_all = pd.read_csv('map_all.csv', index_col=None, header=None)

    # slicing 1st row: chipNumCol, chipNumRow (map_all.csv)
    map_info = map_all.loc[:0,0:CHIP_NUM_COL-1]
    map_info[0] = CHIP_NUM_COL

    # extraction and integration
    for i in range(len(map_all.columns) - CHIP_NUM_COL - 1):
        map_chip = map_all.loc[1:,i:i+CHIP_NUM_COL-1]
        map_chip.columns = map_info.columns
        map_indivisual = pd.concat([map_info, map_chip], join='outer')

        # save csv
        csv_name = 'map_' + format(i, '02') + '.txt'
        map_indivisual.to_csv(csv_name, sep=",", header=False, index=False)

if __name__ == '__main__':
    main()