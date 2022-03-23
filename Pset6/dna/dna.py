import sys
import pandas as pd


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("ERROR")
        return

    file_csv = sys.argv[1]
    sequence = sys.argv[2]
    # TODO: Read database file into a variable
    df = pd.read_csv(file_csv)
    # turning the csv into a dictionary using pandas library
    # you should print the dictionary to know how to work with it.
    dictionary = df.to_dict()
    # TODO: Read DNA sequence file into a variable
    f = open(sequence, "r")
    sequence = f.read()
    f.close()
    # TODO: Find longest match of each STR in DNA sequence
    subsequences = []
    # keep all the subsequences in the given csv into the subsequences list
    for key, value in dictionary.items():
        if key != "name":
            subsequences.append(key)
    # check the longest matches in the given sequence with the longest_match function
    for i in range(len(subsequences)):
        n = longest_match(sequence, subsequences[i])
        # turning the subsequences list into a list of dictionaries, of which one is the name of the
        # subsequence, and its repetition.
        subsequences[i] = {subsequences[i]: n}
    # TODO: Check database for matching profiles
    reapeted_profile = []
    for subsequence in subsequences:
        for key, value in subsequence.items():
            for key1, value1 in dictionary[key].items():
                if value1 == value:
                    reapeted_profile.append(key1)
    set_profile = set(reapeted_profile)
    for n in set_profile:
        if reapeted_profile.count(n) == len(subsequences):
            names = dictionary["name"]
            print(names[n])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
