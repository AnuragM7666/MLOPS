# Problem Summary:
# Read student names and their marks into a dictionary.
# Given a student's name (query_name), compute and print
# the average of their marks rounded to 2 decimal places.
#
# Input Format:
# - First line: integer n (number of students)
# - Next n lines: name and their marks separated by spaces
# - Last line: query_name
#
# Output:
# - Average of query_name's marks, formatted to 2 decimal places.


if __name__ == '__main__':

    n=int(input("Enter number of students: "))

    stud_marks={}

    for _ in range(n):
        #extended iterable unpacking (or sometimes star unpacking). 
        # It allows you to unpack the first element into a variable and the rest into a list.
        name, *score = input().split()
        #map function applies float to each element in score
        # and converts them to a list of floats.
        scores = list(map(float, score))
        stud_marks[name] = scores #It is adding (or updating) an entry in the dictionary stud_marks.
        print(stud_marks)
    query_name = input("Enter student name to query: ")

    query_scores = stud_marks[query_name]
    average = sum(query_scores) / len(query_scores)
    print(f"Average marks obtained by {query_name} is {average:.2f}")