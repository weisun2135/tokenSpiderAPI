import time
from db import Save,Find_id,Update
from setting import START,END,URL
from mytokeSpider import get_page,get_items
import os


def main(page):
    json = get_page(page)

    for mess in get_items(json):

        if mess['id'] == Find_id(mess['id']):
            print('update'+'---'+mess['name'])
            Update(mess['id'],mess)

        elif Find_id(mess['id']) is False:
            Save(mess)
            print(mess)
        else:
            print('stop')
            # return False
            break
            
            



if __name__ == '__main__':

    for i in range(START,END):
        # print(i)
        main(i)
        time.sleep(1)
    os.system('python api.py')