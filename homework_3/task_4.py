'''
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
'''



from typing import List, Dict, AnyStr, Tuple

names = 'Andy Smith, Sam Smith, Andrew MacGonagle, Susan Sunders, Martin Scorcese, Mike Dean, James Collins, Sam Smith'


def thesaurus_adv(names: AnyStr) -> Dict:
    '''
    Description
    :param names: string of full names
    :return: dict of names, where keys are the first letter of name and values are
    '''
    names_list = [x.split() for x in names.split(', ')]
    names_dict = {}
    for name in names_list:
        if name[0][1][0] not in names_dict.keys():
            names_dict[name[1][0]] = {}
            if name[0][0] not in names_dict[name[1][0]].keys():
                names_dict[name[1][0]][name[0][0]] = []
                names_dict[name[1][0]][name[0][0]].append(' '.join(name))
            else:
                names_dict[name[1][0]][name[0][0]].append(' '.join(name))
        else:
            names_dict

    return names_dict


print(thesaurus_adv(names))
