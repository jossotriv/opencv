class grade_calc():
    def __init__(self):
        self.twelvec = 12
        self.ninec = 9
        self.sixc = 6
        self.eighteenc = 18
        self.threec = 3
        self.fifteenc = 15
        # self.perf_credit = 0
        # self.act_credit = 0
        self.credit_list = {'3': self.threec, '6': self.sixc, '9': self.ninec, '12': self.twelvec, '15': self.fifteenc,
                            '18': self.eighteenc}
        self.Grade_list ={'a':5,"b":4,"c":4,"d":1,"e":0}
        self.classes_taken = {}

    def ask(self, Q):
        if Q == "Class":
            a = input("What Class did you take?")
            if type(a) != str:
                return None
            else:
                return a
        if Q == "Credits":
            return self.credit_list[input("How Many Credits was it?")]
        else:
            return self.Grade_list[input("What Grade did you get?").lower()]

    def class_compiler(self):
        flag =0
        while flag == 0:
            if input('Any more Classes? (Y or N)') =="N":
                flag = 1
                break
            Class= self.ask("Class")
            self.classes_taken[Class]=(self.ask("Credits"), self.ask("Grade"))
        return self.classes_taken
    def calculator(self):
        classes = list(self.class_compiler().values())
        credits =[int(i[0]) for i in classes]
        grade =[int(j[1])for j in classes]
        credit_perfect =list(map(lambda x: x*5,credits))
        credit_gained = list(map(lambda x: x*12,grade))
        print("Total Credits Gained: "+str(sum(credit_gained)))
        print("Total Credits Attainable: " + str(sum(credit_perfect)))
        return sum(credit_gained)/sum(credit_perfect) *5.00




        # for i in range(len(self.credit_list)):
        # 	while type(input("How many {} classes have you taken?".format(i))) != int:
        # 	 	input("How many {} classes have you taken?".format(i))
        # 	self.perf_credit += input("How many {} classes have you taken?".format(i))

        # while type(input("How many {} classes have you taken?".format(i))) != int or input("How many {} classes have you taken?".format(i)) > 5:
        # 		input(what was your grade in {}class?)


if __name__ == "__main__":
    calc_grade = grade_calc()

    grade = calc_grade.calculator()

    print(grade)
