import os
import shutil
import re
import sys

# corn = r'C:\Users\papa6\Downloads'  # измените адрес папки
corn = sys.argv[-1]

extensions = {
    'img': ['jpg', 'png', 'bmp', 'gif', 'ico', 'jpeg', 'svg'],
    'vidio': ['avi', 'mp4', 'mov', 'mkv'],
    'document': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'djvu', 'epub'],
    'music': ['mp3', 'ogg', 'wav', 'amr'],
    'archiv': ['zip', 'gz', 'smr'],
    'prj': []
    'Telegram_Desktop': []
}


def normalize(file_name):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    latin_name = file_name.translate(TRANS)  # translate from cyrillic to latin
    # replaces all characters except latin letters and numbers
    niwe_file_name = re.sub(r"[^\w]", "_", latin_name)
    return niwe_file_name


def create_flolderf_from_list(folder_path, folder_names):
    """
    this function creates folders if they are not in the current folder_path
    folder_path - absolute path to the folder
    folder_names - folders with what names will be created
    """

    for folder in folder_names:
        # os.path.exsist - method that checks for the presence of a folder along the path
        if not os.path.exists(f'{folder_path}\\{folder}'):
            # os.mkdir - method created folder
            os.mkdir(f'{folder_path}\\{folder}')


def create_flolder(path, name_folder):
    siquenc = 0
    while os.path.exists(f'{path}\\{name_folder}'):
        without_suff = name_folder.removesuffix(f"_{siquenc}")
        siquenc += 1
        name_folder = f"{without_suff}_{siquenc}"

    if not os.path.exists(f'{path}\\{name_folder}'):
        os.mkdir(f'{path}\\{name_folder}')
        return f'{path}\\{name_folder}'


def file_type_check(file_type, list_folder=extensions):
    """
    check type file, and return folder name

    :param file_type: str
    :param list_folder:
    :return: nam folder
    """
    for fold in list_folder:
        if file_type in list_folder[fold]:
            return fold
    return 'prj'


def folder_view(path, a=1):
    if a == 1:
        create_flolderf_from_list(path, extensions)
    for i in os.listdir(path):  # loop through folder
        if a == 1:
            """
            condition excluding folders that do not need to be sorted by name.
            It is checked by the folder name,
            the name of the folders that are excluded from checking is entered into the dictionary 'extensions'
            """
            if i in extensions:
                continue
        if os.path.isdir(path+"\\"+i):
            """
            recursive traversal of a folder
            """
            folder_view(path+"\\"+i, a+1)
        else:
            split_tup = os.path.splitext(i)
            folder_name = file_type_check(split_tup[1].removeprefix("."))
            file_name = normalize(split_tup[0])
            if split_tup[1].removeprefix(".") in extensions['archiv']:
                unpaking_path = create_flolder(corn+"\\"+'archiv', file_name)
                shutil.unpack_archive(path+"\\"+i, unpaking_path)
                os.remove(path+"\\"+i)
                continue
            elif folder_name == 'prj':
                shutil.move(path + "\\" + i, corn +
                            "\\" + folder_name + "\\" + i)
                continue
            else:
                shutil.move(path+"\\"+i, corn+"\\"+folder_name +
                            "\\"+file_name+split_tup[1])
                continue
        os.rmdir(path+"\\"+i)


folder_view(corn)
