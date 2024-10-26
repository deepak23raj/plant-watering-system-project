plants = [["Aloe Vera", 7], ["Peace Lily", 3], ["Spider Plant", 5], ["Snake Plant", 14], [
    "Fern", 2], ["Cactus", 10], ["Orchid", 7], ["Bamboo", 4], ["Money Plant", 6], ["Lavender", 8]]
count = [["Aloe Vera", 0], ["Peace Lily", 0], ["Spider Plant", 0], ["Snake Plant", 0], [
    "Fern", 0], ["Cactus", 0], ["Orchid", 0], ["Bamboo", 0], ["Money Plant", 0], ["Lavender", 0]]
days_names = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']


def schedule():
    with open('plan.txt', 'w') as file:
        file.write('This is the 12 Weeks watering schedule!')
    with open('plan.txt', 'a') as f:
        for week in range(0, 12):
            f.write('\n\nWeek ' + str(week+1))
            for day in range(0, 7):
                f.write('\n\n'+days_names[day] + ': ')

                if day == 5 or day == 6:
                    for item in count:
                        item[1] = item[1] - 1
                    f.write('Enjoy your weekend!')

                else:
                    for item in count:
                        if item[1] > 0:
                            item[1] = item[1] - 1
                            f.write('\n'+item[0])

                        elif item[1] <= 0:
                            f.write('\n'+item[0] + ':WATER NOW')

                            for element in plants:
                                if element[0] == item[0]:
                                    item[1] = element[1]


schedule()
