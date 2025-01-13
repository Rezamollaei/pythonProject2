import re


def readattendance(file_directory):
    try:
        with open(file_directory, 'r') as file_input:
            reader = file_input.readlines()
            print(reader)
            file_input.close()
    except OSError as problem:
        print('ops we have this problem', problem)

    dic_of_persone = dict()

    for each in reader:
        each = each.strip()
        templist = each.split(',')
        # print(templist)
        dic_of_persone[templist[0]] = {'contact': templist[1], 'entry': int(templist[2]), 'exit': int(templist[3])}
    # print(dic_of_persone)
    return dic_of_persone


def read_file(file_directory):
    try:
        with open(file_directory, 'r') as file_input:
            reader = file_input.readline()
            print(reader)
            file_input.close()
    except OSError as problem:
        print('ops we have this problem', problem)
    for persone in reader:
        persone = persone.strip()
    list_of_persone = []
    list_of_persone.append(persone)
    return list_of_persone


def find(list_persone, dict_persone):
    for persone in list_persone:
        list_of_sus = []
        flag = 0
        for each in dict_persone:
            if dict_persone[each]['entry'] <= dict_persone[persone]['entry'] <= dict_persone[each]['exit'] or \
                    dict_persone[each]['entry'] <= dict_persone[persone]['exit'] <= dict_persone[each][
                'exit'] and persone != each:
                print(each)
                list_of_sus.append(each)
                flag = 1
        if flag == 0:
            print('costum contact  , {persone} : **')

        sorted_list = sorted(list_of_sus)
        for every in sorted_list:
            print(f'contact with {every} , number {dict_persone[every][contact]}')


def main():
    file_path1 = 'attendance.txt'
    file_path2 = 'suspicious.txt'
    print(readattendance(file_path1))
    print(read_file(file_path2))


if __name__ == '__main__':
    main()

