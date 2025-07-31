import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="This program analyzes patterns in its input")
    parser.add_argument("-dataType", default="word", choices=["long", "line", "word"],
                        help="Choose an option from the list")
    parser.add_argument("-sortIntegers", action="store_true")

    return parser.parse_args()

def find_largest(data:list, data_type:str, sort_integers:bool) -> int|str:
    """Returns the largest element in a list (by length if the list consists of strings)
    according to the arguments passed when firing the program"""
    if data_type == 'long' or sort_integers:
        return max(data)
    else:
        return max(data, key=len)

def count_element(data:list, element:int|str) -> tuple:
    """Returns the count of an element in a list as well as its percentage of appearance"""
    count = sum(1 for el in data if el == element)
    percentage = (count * 100) // len(data)

    return count, percentage

def print_analysis(data:list, element:int|str, count:int, percentage:int, data_type:str, sort_integers:bool) -> None:
    """Prints the analysis of the patterns in data depending on the arguments passed"""
    if sort_integers:
        print(f"Total numbers: {len(data)}.")
        sorted_data = [str(x) for x in sorted(data)]
        print(f"Sorted data: {' '.join(sorted_data)}")
    else:
        if data_type == 'long':
            print(f"Total numbers: {len(data)}.")
            print(f"The greatest number: {element} ({count} time(s), {percentage}%).")
        elif data_type == 'word':
            print(f"Total words: {len(data)}.")
            print(f"The longest word: {element} ({count} time(s), {percentage}%).")
        else:
            print(f"Total lines: {len(data)}.")
            print(f"The longest line:")
            print(f"{element}")
            print(f"({count} time(s), {percentage}%).")

def main():
    args = parse_arguments()

    # get data from input until EOF (Ctrl+D)
    data_list = []
    while True:
        try:
            data = input()

            if args.dataType == 'long' or args.sortIntegers:
                data_line = [int(x) for x in data.split()]
                data_list.extend(data_line)
            elif args.dataType == 'word':
                data_line = data.split()
                data_list.extend(data_line)
            else:
                data_list.append(data)

        except EOFError:
            break

    # print analysis
    largest_element = find_largest(data_list, args.dataType, args.sortIntegers)
    largest_count, largest_percentage = count_element(data_list, largest_element)

    print_analysis(data_list, largest_element, largest_count, largest_percentage, args.dataType, args.sortIntegers)


if __name__ == "__main__":
    main()