import typing
students = ["Elijah Evans", "Charissa Mueller", "Kirby Park",
     "Jescie Hill",
     "Leroy Herring",
     "Francis Castaneda",
     "Bree Gregory",
     "Kermit Stevens",
     "Jordan Terry",
     "Paul Trujillo",
     "Linda Beck",
     "Dara Mckinney",
     "Idola Pearson",
     "Phelan Vazquez",
     "Cleo Dyer",
     "Kameko Mccall",
     "Kitra Tillman",
     "Oren Miles",
     "Martin Kerr",
     "Orlando Noble",
     "Ferdinand Carr",
     "Scott Norman",
     "Autumn Winters",
     "Phillip Heath",
     "Ryder Mueller",
     "Armand Lucas",
     "Naida Hart",
     "Deborah Spencer",
     "Blythe Kidd",
     "Colleen Keller"]


def ejercicio_1_1():
    for i in students:
        students.append(i.lower().replace(" ", "_"))
        
        print(students)
