import os
from typing import Any

import openindirfile



def to_do_logic(
    param_json: dict = None,
    ex_model_param: dict = None,
    in_dir: str = None,
    out_dir: str = None,
    ex_out_dir: str = None,
    is_training: bool = False,
    training_model_path: str = None,
) -> Any: 

    accuracy_json, loss_json, output_params, files = openindirfile.to_open_file(
        in_dir=in_dir,
        out_dir=out_dir,
        paramjson=param_json
    )

    return accuracy_json, loss_json, output_params, files

if __name__ == "__main__":
    openindirfile.to_open_file(in_dir=f'{os.getcwd()}{os.sep}indir',out_dir=f'{os.getcwd()}{os.sep}outdir')
    
    