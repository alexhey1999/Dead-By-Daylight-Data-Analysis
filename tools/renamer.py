from os import rename, listdir
import os
from dotenv import load_dotenv,find_dotenv
import re
import string


def main(file_location):
    for i in listdir(file_location):
        try:
            new_perk_name = i.split('_')[1].split('.')[0]
            new_perk_name = re.sub('([a-zA-Z0-9])', lambda x: x.groups()[0].upper(), new_perk_name, 1)        
            new_perk_name = ' '.join(re.findall('[A-Z][^A-Z]*',new_perk_name))
            print(file_location+'/'+i)
            print(new_perk_name+'.png')
            rename(file_location+'/'+i,file_location+'/'+new_perk_name+'.png')
            print(f"{i} renamed named - SUCCESS")
        except:
            print(f"{i} incorrectly named - CAUTION")
    

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    
    folder_root = "./Images/Addons/"
    for i in listdir(folder_root):
        main(f'{folder_root}{i}/')
            
    # os.getenv('PERK_LOCATION_SURVIVOR')
    # main(os.getenv('PERK_LOCATION_SURVIVOR'))
    # main('./Images/Items/')

