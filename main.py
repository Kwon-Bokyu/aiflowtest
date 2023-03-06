import os
from typing import Any
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import abc_re

def to_open_file(in_dir: str , out_dir: str, paramjson: dict = None, stoplist: list = None, wantlist: list = None):
    indir_file = os.listdir(in_dir)
    if wantlist:
        indir_file = wantlist
    if stoplist:
        for i in stoplist:
            indir_file.remove(i)
        
    document = []
    for i, file_name in enumerate(indir_file):
        to_do_logic(in_dir=in_dir, out_dir=out_dir, indir_file=file_name)

def to_do_logic(
    param_json: dict = None,
    ex_model_param: dict = None,
    in_dir: str = None,
    out_dir: str = None,
    ex_out_dir: str = None,
    is_training: bool = False,
    training_model_path: str = None,
) -> Any: 
    # print("far")
    print(out_dir)
    sales = pd.read_csv(f'{in_dir}{os.sep}sales_data_sample_utf8.csv')
    sales = sales.drop_duplicates()
    sales_clean = sales.copy()
    grouped = sales_clean.groupby("PRODUCTCODE").agg(total_sales=('QUANTITYORDERED', np.sum), total_revenue=('SALES', np.sum)).reset_index()

    
    
    abc = abc_re.ABC_BY_HO(grouped[['PRODUCTCODE', 'total_sales']])
    
    plt.figure(1)
    sns.countplot(x = 'Category', data = abc).set(title = 'No. of A, B, and C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}No. of A, B, and C Cat. Items for All Countries.png')
    
    plt.figure(2)
    sns.barplot(x = 'Category', y = 'total_sales', data = abc).set(title = 'Avg. Value of A, B, and C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}Avg. Value of A, B, and C Cat. Items for All Countries.png')
    
    mc_abc = abc_re.productmix(grouped['PRODUCTCODE'], grouped['total_sales'], grouped['total_revenue'])

    plt.figure(3)
    sns.countplot(x = 'product_mix', data = mc_abc).set(title = 'No. of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}No. of A_A to C_C Cat. Items for All Countries.png')

    plt.figure(4)
    sns.barplot(x = 'product_mix', y = 'sales', data = mc_abc).set(title = 'Avg. Value of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}Avg. Value of A_A to C_C Cat. Items for All Countries.png')

    plt.figure(5)
    sns.barplot(x = 'product_mix', y = 'revenue', data = mc_abc).set(title = 'Total Revenue of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}Total Revenue of A_A to C_C Cat. Items for All Countries.png')
    
    # result_data = abc.to_json(orient='records')
    # result_data_mcabc = mc_abc.to_json(orient='records')
    

    abc.to_csv(f'{out_dir}/abc_single.csv', index = False, header=True)
    mc_abc.to_csv(f'{out_dir}/abc_multi.csv', index = False, header=True)
    
    return None, None, {}, ["abc_multi.csv", "abc_single.csv", "No. of A, B, and C Cat. Items for All Countries.png", 'Avg. Value of A, B, and C Cat. Items for All Countries.png',"Avg. Value of A_A to C_C Cat. Items for All Countries.png", "No. of A_A to C_C Cat. Items for All Countries.png", "Total Revenue of A_A to C_C Cat. Items for All Countries.png"]



if __name__ == "__main__":
    to_do_logic(in_dir=f'{os.getcwd()}{os.sep}indir',out_dir=f'{os.getcwd()}{os.sep}outdir')
    
    