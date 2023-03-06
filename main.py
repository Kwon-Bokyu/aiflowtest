import os
import openindirfile



if __name__ == "__main__":
    openindirfile.to_open_file(in_dir=f'{os.getcwd()}{os.sep}indir',out_dir=f'{os.getcwd()}{os.sep}outdir')
    
    