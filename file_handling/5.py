class FileMerger:

    def __init__(self, file1, file2, output_file):
        self.file1 = file1
        self.file2 = file2
        self.output_file = output_file

    def merge_files(self):
        with open(self.file1, "r") as f1, open(self.file2, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()

        with open(self.output_file, "w") as out:
            out.write(content1)
            out.write(content2)

merger = FileMerger("file1.txt", "file2.txt", "merged.txt")
merger.merge_files()