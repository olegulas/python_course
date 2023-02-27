from os import path

file_data = list()
id_last = 0
db_tel = "db_tel.txt"
newline = "\n"


def open_file():
    if not path.exists(db_tel):
        with open(db_tel, "w", encoding="utf-8"):
            print("Create new db_file done!")


def read_data():
    global file_data, id_last

    with open(db_tel, "r", encoding="utf-8") as file:
        file_data = [i.strip() for i in file]
        if file_data:
            id_last = int(file_data[-1][0])

        return file_data


def show_data():
    if not file_data:
        print("Empty file, no data!")
    else:
        print(*file_data, sep=newline)


def add_new_record():
    data = ['surname', 'name', 'second_name', 'phone']
    date_list = list()

    for i in data:
        date_list.append(data_collection(i))

    if not record_exist(0, " ".join(date_list)):
        id_last += 1
        date_list.insert(0, str(id_last))

        with open(db_tel, 'a', encoding="utf-8") as file:
            file.write(f'{" ".join(date_list)}{newline}')
        print(f"The record added in database!{newline}")
    else:
        print("The data already exists!")


def del_record():
    global file_data, id_last
    show_data()

    del_rec = input("Enter ID: ")

    if record_exist(del_rec, ""):
        file_data = [i for i in file_data if i[0] != del_rec]
        with open(db_tel, 'w', encoding="utf-8") as file:
            file.write(f'{newline.join(file_data)}{newline}')
        print(f"Record deleted!{newline}")
    else:
        print("ID is not correct!")


def change_record(data_rec):
    id_rec, data_num, data = data_rec

    for i, j in enumerate(file_data):
        if j[0] == id_rec:
            j = j.split()
            j[int(data_num)] = data
            if record_exist(0, " ".join(j[1:])):
                print("The data already exists!")
                return
            file_data[i] = " ".join(j)
            break

    with open(db_tel, 'w', encoding="utf-8") as file:
        file.write(f'{newline.join(file_data)}{newline}')
    print(f"Record changed!{newline}")


def search_contact():
    search_data = record_exist(0, input("Enter the search data: "))
    if search_data:
        print(*search_data, sep=newline)
    else:
        print("The data is not correct!")


def record_exist(rec_id, data):
    if rec_id:
        record = [i for i in file_data if rec_id in i[0]]
    else:
        record = [i for i in file_data if data in i]
    return record


def data_collection(num):
    ans = input(f"Enter a {num}: ")
    while True:
        if num in "surname name second_name":
            if ans.isalpha():
                break
        if num == "phone number":
            if ans.isdigit() and len(ans) == 11:
                break
        ans = input(f"Data is incorrect!{newline}"
                    f"Use only use only the letters"
                    f" of the alphabet, the length"
                    f" of the number is 11 digits{newline}"
                    f"Enter a {num}: ")
    return ans


def menu():
    open_file()
    play = True
    while play:
        read_data()
        ans = input(f"Phone book database:{newline}"
                    f"1. Show all date in base{newline}"
                    f"2. Add a new record{newline}"
                    f"3. Search data{newline}"
                    f"4. Change data{newline}"
                    f"5. Delete data{newline}"
                    f"6. Export/Import data{newline}"
                    f"7. Exit{newline}")
        match ans:
            case "1":
                show_data()
            case "2":
                add_new_record()
            case "3":
                search_contact()
            case "4":
                done = edit_menu()
                if done:
                    change_record(done)
            case "5":
                del_record()
            case "6":
                export_menu()
            case "7":
                play = False
            case _:
                print(f"Please, try again!{newline}")


def edit_menu():
    add_dict = {"1": "surname", "2": "name", "3": "second name", "4": "phone"}

    show_data()
    record_id = input("Enter the record id: ")

    if record_exist(record_id, ""):
        while True:
            print(f"{newline}Changing:")
            change = input(f"1. surname{newline}"
                           f"2. name{newline}"
                           f"3. patronymic{newline}"
                           f"4. phone number{newline}"
                           f"5. exit{newline}")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")


def exp_bd(name):
    if not path.exists(name):
        with open(f"{name}.txt", "w", encoding="utf-8") as file:
            file.write(f'{newline.join(file_data)}{newline}')


def import_bd(name):
    global db_tel
    if path.exists(name):
        db_tel = name
        read_data()


def export_menu():
    while True:
        print(f"{newline}Export/Import menu:")
        ans = input(f"1. Import data{newline}"
                    f"2. Export data{newline}"
                    f"3. Exit{newline}")

        match ans:
            case "1":
                import_bd(input("Enter the name file: "))
            case "2":
                exp_bd(input("Enter the name file: "))
            case "3":
                return 0
            case _:
                print("The data is not recognized, repeat the input.")


if __name__ == "__main__":
    menu()
