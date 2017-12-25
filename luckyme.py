import numpy.random as rand
rand.seed(int((69 + 15 + 7)/3))

def print_list(a):
    for item, i in zip(a, range(1, len(a) + 1)):
        print(i, '\t'*2, item)


def perform(people, stuff):
    for thing in stuff:
        lucky_one = rand.randint(0, len(people))
        print(thing, '\t'*2 ,'-'*10 + '>', people[lucky_one])
        del people[lucky_one]

def main():
    lucky_people = ["Білоус Анастасія Сергіївна",
                    "Богдан Валентин Вікторович",
                    "Дітковська Юлія Василівна",
                    "Зінченко Анастасія Олександрівна",
                    "Климчук Анастасія Романівна",
                    "Олесюк Інна Юріївна",
                    "Панченко Денис Володимирович",
                    "Ревуцька Людмила Олександрівна",
                    "Свириденко Віталій Олександрович",
                    "Сич Дмитро Вікторович",
                    "Сільченко Дарина Володимирівна",
                    "Соколов Володимир Володимирович",
                    "Стельмащук Мар’яна Миколаївна",
                    "Степаненко Євгеній Юрійович",
                    "Степенко Богдан Валентинович",
                    "Терещенко Катерина Миколаївна",
                    "Титаренко Андрій Миколайович",
                    "Токмакова Дар'я Сергiївна",
                    "Троян Макар Романович",
                    "Тюріна Марія Олександрівна",
                    "Хворостяний Анатолій Олександрович",
                    "Худецький Михайло Анатолійович",
                    "Цибульський Іван Сергійович",
                    "Шинкарук Юлія Вадимівна",
                    "Шуліков Арсеній Владиславович",
                    "Шульженко Яна Олегівна",
                    "Юрчук Максим Віталійович",
                    "Якубець Андрій Олександрович"
                    ]

    goods = ["ЧМ А", "Мухин +10", "Мухин +5", "Мухин +5", "Зайка +10", "Зайка +10"]

    out = ["Зінченко Анастасія Олександрівна", "Сільченко Дарина Володимирівна", "Степенко Богдан Валентинович"]

    for outer in out:
        lucky_people.remove(outer)
    print_list(lucky_people)
    print('-'*10)
    print('RESULTS:')
    print('-'*10)
    perform(lucky_people, goods)

if __name__=='__main__':
    main()