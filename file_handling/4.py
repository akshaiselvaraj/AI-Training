class DatasetCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    def clean_line(self, line):
        line = line.strip()        
        line = line.lower()       
        line = line.replace("!", "") 
        return line

    def process_file(self):
        with open(self.input_file, "r") as infile, open(self.output_file, "w") as outfile:
            for line in infile:
                cleaned = self.clean_line(line)
                outfile.write(cleaned + "\n")


cleaner = DatasetCleaner("reviews.txt", "clean_reviews.txt")
cleaner.process_file()

print("Cleaned dataset saved to clean_reviews.txt")