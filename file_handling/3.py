class LineCounter:
    def __init__(self, file_name):
        self.file_name = file_name

    def count_lines(self):
        count = 0

        with open(self.file_name, "r") as file:
            for line in file:
                count += 1
        return count

counter = LineCounter("dataset.txt")
total_lines = counter.count_lines()
print("Total number of lines:", total_lines)