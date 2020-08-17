import os
def create():

    if not os.path.exists('files'):
        os.makedirs('files')

    file_ins = open('files/install_info.txt', 'w')
    file_ins.write('Test')
    file_ins.close()

    file_all = open('files/all_packages.txt', 'w')
    file_all.write('Test')
    file_all.close()

    file_show = open('files/show_info.txt', 'w')
    file_show.write('Test')
    file_show.close()