from datetime import datetime, timedelta

plants = [["Aloe Vera", 7], ["Peace Lily", 3], ["Spider Plant", 5], ["Snake Plant", 14], [
    "Fern", 2], ["Cactus", 10], ["Orchid", 7], ["Bamboo", 4], ["Money Plant", 6], ["Lavender", 8]]
count = [["Aloe Vera", 0], ["Peace Lily", 0], ["Spider Plant", 0], ["Snake Plant", 0], [
    "Fern", 0], ["Cactus", 0], ["Orchid", 0], ["Bamboo", 0], ["Money Plant", 0], ["Lavender", 0]]
days_names = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_next_monday():
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    return today + timedelta(days=days_until_monday)


def schedule():
    start_date = get_next_monday()
    with open('plan.txt', 'w') as file:
        file.write('This is the 12 Weeks watering schedule!')
    with open('plan.txt', 'a') as f:
        current_date = start_date
        for week in range(12):
            f.write(f'\n\nWeek {week + 1}')
            for day in range(7):
                day_name = days_names[day]
                formatted_date = current_date.strftime('%d/%m/%Y')
                f.write(f'\n\n{day_name}, {formatted_date}: ')

                if day_name in ['Saturday', 'Sunday']:
                    for item in count:
                        item[1] = item[1] - 1
                    f.write('Enjoy your weekend!')

                else:
                    for item in count:
                        if item[1] > 0:
                            item[1] = item[1] - 1
                            f.write(f'\n{item[0]}')

                        elif item[1] <= 0:
                            f.write(f'\n{item[0]}: WATER NOW')

                            for element in plants:
                                if element[0] == item[0]:
                                    item[1] = element[1]

                current_date += timedelta(days=1)


schedule()
