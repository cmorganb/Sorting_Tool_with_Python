import argparse
from collections import Counter

def parse_arguments():
    parser = argparse.ArgumentParser(description="This program analyzes patterns in its input")
    parser.add_argument("-dataType", default="word", choices=["long", "line", "word"],
                        help="Choose an option from the list")
    parser.add_argument("-sortingType", default="natural", choices=["byCount", "natural"])

    return parser.parse_args()

def print_analysis(data:list, data_type:str, sorting_type:str) -> None:
    """Prints the analysis of the patterns in data depending on the arguments passed"""
    if sorting_type == "byCount":
        if data_type == "long":
            print(f"Total numbers: {len(data)}.")
        elif data_type == 'word':
            print(f"Total words: {len(data)}.")
        else:
            print(f"Total lines: {len(data)}.")

        counts = Counter(data)
        no_duplicates = list(set(data))
        no_duplicates.sort()
        sorted_data = sorted(no_duplicates, key=lambda x: counts[x])
        for long in sorted_data:
            print(f"{long}: {counts[long]} time(s), {(counts[long] * 100) // len(data)}%")
    else:
        if data_type == "long":
            print(f"Total numbers: {len(data)}.")
            sorted_data = [str(x) for x in sorted(data)]
            print(f"Sorted data: {' '.join(sorted_data)}")
        elif data_type == 'word':
            print(f"Total words: {len(data)}.")
            sorted_data = sorted(data)
            print(f"Sorted data: {' '.join(sorted_data)}")
        else:
            print(f"Total lines: {len(data)}.")
            sorted_data = sorted(data)
            print("Sorted data:")
            for line in sorted_data:
                print(line)

def main():
    args = parse_arguments()

    # get data from input until EOF (Ctrl+D)
    data_list = []
    while True:
        try:
            data = input()

            if args.dataType == 'long':
                data_line = [int(x) for x in data.split()]
                data_list.extend(data_line)
            elif args.dataType == 'word':
                data_line = data.split()
                data_list.extend(data_line)
            else:
                data_list.append(data)

        except EOFError:
            break

    print_analysis(data_list, args.dataType, args.sortingType)


if __name__ == "__main__":
    main()