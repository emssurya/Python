subject = ["Cryptograpy","Python","Mathemetics","Enironment","Python Lab","Machin Learning"]
subjcode = ["CY-102","PY-114","MA-111","CS-107","PL-107","ML-101"]

internal_marks =[]
sem_marks=[]
count=MTotal=0

name= input("Enter your name:")
fname=input("Enter your fathe name:")
rnumber=input("Enter your roll number:")
College=input("Enter your college name:")
for x in subject:
    a=int(input("Enter internal term marks for" +x))
    b=int(input("Enter semester marks for" +x))
    internal_marks.append(a)
    sem_marks.append(b)
print("\n\n\t\t******************************YOUR RESULT******************************\n\n\t\t")
print("\t\t COLLEGE:",college)
print("\n\t\ tNAME:",name,"\t\tFATER NAME:",fname)

print("\n\t\t ROLL NUMBER:",rnumber)
print("\n\t\t SUBJECTS \tMARKS1 \tMARKS2 \tTOTAL")

for (x,y,z)in zip(Subjcode, internal_marks, sem_marks):
    print("\n\t\t","\t",y,"\t",z,"\t",y+z)
    MTotal=MTotal+y+z
    if y+z<44:
        count=count+1
        if count==0:
            print("\n\t\t TOTAL MARKS:",MTotal,"\t\tRESULT:PASS")
else:
     print("\n\t\tTOTAL MARKS:",MTotal,"\t\tRESULT:FAIL")
                
