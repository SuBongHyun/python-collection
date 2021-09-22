#같은 경로에서 directory생성하기

import os
dir_data= './datasets'
dir_save=os.path.join(dir_data, 'train')
if not os.path.exists(dir_save):
    os.makedirs(dir_save)
    
