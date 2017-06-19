def main():
    print_header()
    run_event_loop()

def print_header():
    print('------------------------------------')
    print('       THE JOURNAL APP              ')
    print('------------------------------------')
    print()


def run_event_loop():
    user_name = input("Please input your name: ")
    print("What do you want to do with your Journal {} :)".format(user_name))
    cmd = None
    journal_data = list()

    while cmd != "x":
        cmd = input("[L]ist of entries, [A]dd an entry or E[x]it the Journal: ")
        if cmd.lower().strip() == "l":
            list_entries(journal_data)
        elif cmd.lower().strip() == "a":
            add_entries(journal_data)
        elif cmd.lower().strip() != "x":
            print("Sorry {} we do not understand this ({}) input".format(user_name, cmd))

    print("Goodbye {} .Exiting your Journal Now!!!".format(user_name))


def list_entries(data):
    print("Your journal entries are as follows: ")
    reversed_entries = reversed(data)
    for index, entry in enumerate(reversed_entries):
        print("* [{}]{}".format(index + 1, entry))


def add_entries(data):
    text = input ("Type your entry, <enter> to exit: ")
    data.append(text)


main()