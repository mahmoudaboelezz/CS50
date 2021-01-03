import sys
import csv


# Identifies person
class DnaIdentifier:
    def __init__(self):
        pass

    def get_strs(self, dic):
        strs = []
        for key in dic.keys():
            if key != "name":
                strs.append(key)
        return strs

    def check_dna(self, strs_cpy, dna_cpy):
        dna = dna_cpy.copy()
        strs = strs_cpy.copy()
        counter = {}
        streak = ("", 0)
        for gene in strs:
            counter.update({gene: 0})

        while dna != []:
            match = False
            for gene in strs:
                match = True
                try:
                    for idx, char in enumerate(gene):
                        if char != dna[idx]:
                            match = False
                            break
                except IndexError:
                    match = False
                    strs.pop(strs.index(gene))

                if match:
                    if streak[0] == "":
                        streak = (gene, 1)
                    elif gene == streak[0]:
                        streak = (streak[0], streak[1]+1)
                        print("Streak Up: " + gene + " " + str(streak[1]))
                        print(dna)
                    else:
                        if streak[1] > counter[streak[0]]:
                            counter[streak[0]] = streak[1]
                        streak = (gene, 1)
                    dna = dna[len(gene):]
                    if len(dna) < 2:
                        if streak[1] > counter[streak[0]]:
                            counter[streak[0]] = streak[1]
                    break
            if not match:
                if streak[0] != "":
                    if streak[1] > counter[streak[0]]:
                        counter[streak[0]] = streak[1]
                    streak = ("", 0)
                dna = dna[1:]

        return counter
    
    def identify_person(self, database_cpy, dna):
        database = database_cpy.copy()
        strs = self.get_strs(database[0])
        str_counts = self.check_dna(strs, dna)
        for key in str_counts.keys():
            str_counts[key] = str(str_counts[key])
        print(str_counts)
        for dic in database:
            name = dic["name"]
            dic.pop("name")
            if dic == str_counts:
                return name
        return "No match"



def main():
    # Make sure two parameters are entered
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Reading database
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    # Reading dna
    with open(sys.argv[2]) as file:
        dna = list(file.read())

    # Identify person
#    blah = ['G', 'A', 'A', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C', 'A', 'G', 'A', 'T', 'C']
    identifier = DnaIdentifier()
    person = identifier.identify_person(database, dna)
    print(person)


if __name__ == "__main__":
    main()

