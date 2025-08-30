# HCGAN
Speech super-resolution

# File Overview

- `create_meta_files.py` - Used to create corresponding path files for training and validation.
- e.g. 4-16k experiment:
  `python data_prep/create_meta_files.py <path for 4 kHz data> egs/vctk/4-16 lr`
  
  `python data_prep/create_meta_files.py <path for 16 kHz data> egs/vctk/4-16 hr`
  
- `train.py` - Used to create corresponding path files for training and validation.
- `predict_multi.py` - Used to create corresponding path files for training and validation.

# How to use
1. Install all requirements
2. ​Configure paths
3. Run create_meta_files.py
4. Run train.py
