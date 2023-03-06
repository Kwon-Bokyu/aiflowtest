import os
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
        
    #wantlist = ["a.csv", "b.csv"]
    document = []
    for i, file_name in enumerate(indir_file):
        to_do_logic(in_dir=in_dir, out_dir=out_dir, indir_file=file_name)
        # if i == 0:
        #     document = pd.read_csv(f'{in_dir}{os.sep}{file_name}')
        # else:
        #     document.append(pd.read_csv(f'{in_dir}{os.sep}{file_name}'))
        


    
def to_do_logic(in_dir: str , out_dir: str, indir_file: str, paramjson: dict = None):
    # print("far")
    print(out_dir)
    sales = pd.read_csv(f'{in_dir}{os.sep}{indir_file}')
    sales = sales.drop_duplicates()
    sales_clean = sales.copy()
    grouped = sales_clean.groupby("PRODUCTCODE").agg(total_sales=('QUANTITYORDERED', np.sum), total_revenue=('SALES', np.sum)).reset_index()

    
    
    abc = abc_re.ABC_BY_HO(grouped[['PRODUCTCODE', 'total_sales']])
    
    sns.countplot(x = 'Category', data = abc).set(title = 'No. of A, B, and C Cat. Items for All Countries')
    sns.barplot(x = 'Category', y = 'total_sales', data = abc).set(title = 'Avg. Value of A, B, and C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}/Avg. Value of A, B, and C Cat. Items for All Countries.png')
    
    mc_abc = abc_re.productmix(grouped['PRODUCTCODE'], grouped['total_sales'], grouped['total_revenue'])
    
    sns.countplot(x = 'product_mix', data = mc_abc).set(title = 'No. of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}No. of A_A to C_C Cat. Items for All Countries.png')
    sns.barplot(x = 'product_mix', y = 'sales', data = mc_abc).set(title = 'Avg. Value of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}Avg. Value of A, B, and C Cat. Items for All Countries.png')
    sns.barplot(x = 'product_mix', y = 'revenue', data = mc_abc).set(title = 'Total Revenue of A_A to C_C Cat. Items for All Countries')
    plt.savefig(f'{out_dir}{os.sep}Total Revenue of A_A to C_C Cat. Items for All Countries.png')
    
    # result_data = abc.to_json(orient='records')
    # result_data_mcabc = mc_abc.to_json(orient='records')
    

    abc.to_csv(f'{out_dir}/abc_single.csv', index = False, header=True)
    mc_abc.to_csv(f'{out_dir}/abc_multi.csv', index = False, header=True)
    
    return None
