class CustomCSV():
    def __init__(self,filename):
        self.filename=filename

    def read_data(self):
        headers=[]
        rows=[]

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

                if not lines:
                    return headers, rows

                headers = lines[0].strip().split(",")


                for line in lines[1:]:
                    rows.append(line.strip().split(","))

        except FileNotFoundError:
            print("file not found")

        return headers,rows

    def get_headers(self):
        headers,_=self.read_data()
        return headers

    def get_rows(self):
        _,rows=self.read_data()
        return rows



    def delete_row(self,linenumber):

        if linenumber>=1 :
            try:
                with open(self.filename, "r") as file:
                    lines = file.readlines()

                    if linenumber>=len(lines):
                        print("line is out of range")
                        return

                    print("Before deletion:", lines[linenumber].strip())
                    lines.pop(linenumber)

                with open(self.filename, "w") as file:
                    file.writelines(lines)
                print("After Deletion: line was compeletely removed")

            except FileNotFoundError:
                print("file not found:",self.filename)
        else:
            print("headers is preserved")


    def replace_row(self,linenumber,new_row):
        if linenumber >= 1:
            try:
                with open(self.filename, "r") as file:
                    lines = file.readlines()

                    if linenumber >= len(lines):
                        print("line is out of range")
                        return

                    print("Original:", lines[linenumber].strip())

                    new_line=",".join(new_row)+"\n"



                    lines[linenumber]=new_line



                with open(self.filename, "w") as file:
                    file.writelines(lines)
                print("Replaced with:", new_line.strip())

            except FileNotFoundError:
                print("file not found:", self.filename)
        else:
            print("headers is preserved")


    def copy_file(self,backupfile):
        try:
            with open(self.filename, "r") as fil:
                with open(backupfile, "w") as bac:
                    bac.write(fil.read())

        except:
            print("file not found:", self.filename)


    def clear_file(self):
        headers,rows=self.read_data()
        with open(self.filename,"w") as file:
            file.write(",".join(headers)+"\n")






