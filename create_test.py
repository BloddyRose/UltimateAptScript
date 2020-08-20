import os

"""
    This is function that create the files that are required by the ultimateapt to have
    I have put the in another py file so the program will not be slow
"""


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

    file_up = open('files/update.txt', 'w')
    file_up.write('Test')
    file_up.close()

    file_upgr = open('files/upgrade.txt', 'w')
    file_upgr.write('Test')
    file_upgr.close()

    file_s = open('files/satisfy.txt', 'w')
    file_s.write('Test')
    file_s.close()

    file_r = open('files/removed.txt', 'w')
    file_r.write('Test')
    file_r.close()

    file_ar = open('files/autoremove.txt', 'w')
    file_ar.write('Test')
    file_ar.close()

    file_sr = open('files/search.txt', 'w')
    file_sr.write('Test')
    file_sr.close()
