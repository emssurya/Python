subject = ["Cryptography", "Python", "Mathematics", "Environment", "Python Lab", "Machine Learning"]
subjcode = ["CY-102", "PY-114", "MA-111", "CS-107", "PL-107", "ML-101"]

internal_marks = []
sem_marks = []
count = 0
MTotal = 0

name = input("Enter your name: ")
fname = input("Enter your father's name: ")
rnumber = input("Enter your roll number: ")
college = input("Enter your college name: ")

for x in subject:
    a = int(input("Enter internal term marks for " + x + ": "))
    b = int(input("Enter semester marks for " + x + ": "))
    internal_marks.append(a)
    sem_marks.append(b)

print("\n\n\t\t****************************** YOUR RESULT ******************************\n\n")
print("\t\tCOLLEGE:", college)
print("\t\tNAME:", name, "\t\tFATHER'S NAME:", fname)
print("\t\tROLL NUMBER:", rnumber)
print("\n\t\tSUBJECT CODE\tINTERNAL\tSEMESTER\tTOTAL")

for (code, internal, sem) in zip(subjcode, internal_marks, sem_marks):
    total = internal + sem
    print(f"\t\t{code}\t\t{internal}\t\t{sem}\t\t{total}")
    MTotal += total
    if total < 44:
        count += 1

if count == 0:
    print(f"\n\t\tTOTAL MARKS: {MTotal}\t\tRESULT: PASS")
else:
    print(f"\n\t\tTOTAL MARKS: {MTotal}\t\tRESULT: FAIL")
