class Searching:
    def __init__(self, lst):
        # self.lst = sorted(lst)
        self.lst = lst
        self.lst_len = len(lst)

    def linear_search(self, find):
        if self.lst_len == 0:
            return "List is Empty"

        posi = 0
        iteration = 0
        while posi < self.lst_len:
            iteration += 1
            if self.lst[posi] == find:
                return f"Found {find} at {posi} in list and took {iteration} iterations"
            posi += 1

        return f"{find} not found in list"

    def binary_search(self, find):
        if self.lst_len == 0:
            return "List is Empty"

        start, end = 0, self.lst_len - 1

        iteration = 0
        while start <= end:
            iteration += 1
            mid = (start + end) // 2
            if self.lst[mid] == find:
                return f"Found {find} at {mid} in list and took {iteration} iterations"
            elif self.lst[mid] < find:
                start = mid + 1
            elif self.lst[mid] > find:
                end = mid - 1

        return f"{find} not found in list"


search = Searching(list(range(100000000)))
find = int(input("Enter number to find : "))
print(f"\nLinear Search\n{search.linear_search(find)}")
print(f"\nBinary Search\n{search.binary_search(find)}")
