## Classes Solutions (009)

1. Write your own class-- Class name is student

        class student:
            def __init__(self, name, year, age, housing, classes, major, intern):
                self.name = name
                self.year = year
                self.age = age
                self.housing = housing
                self.classes = classes
                self.major = major
                self.intern = intern

   
3. Functions of the class should profile student:
        a. year of student
        b. where are they staying
        c. how many classes are they taking
        d. are they taking an internship
        e. age

        def display_info(self):
            return f"{self.name} {self.year} {self.age} {self.housing} {self.classes} {self.major} {self.intern}"

5. Call the class

        student1 = student("Mlynn", "senior", 21, "off_campus", 5, "marine_science", "yes")
        print(student1.display_info())
        
        student2 = student("Olivia", "senior", 21, "off_campus", 6, "communications", "yes")
        print(student2.display_info())
        
        student3 = student("Matt", "junior", 19, "hilltop", 9, "music_ed", "no")
        print(student3.display_info())

7. Print a profile of a specific student

       print(student3.display_info())
       Matt junior 19 hilltop 9 music_ed no