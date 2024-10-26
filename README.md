# Plant Watering System

The Plant Watering System program allows the user to create a 12-week plant watering schedule that includes the following features:

- Each plant has it's own watering frequency and this is taken into account by the schedule.
- The program avoids weekend watering for work-life balance, even if the plant’s schedule suggests watering on a Saturday or Sunday.
- The schedule outputs "WATER NOW" when a plant needs watering, otherwise it simply displays the plant's name without this prompt.
- Once the program (stored in plant-watering-system.py) runs, the schedule is saved in plan.txt. The plan.txt file will start empty and be populated with the complete schedule upon execution.

The program is designed to be simple yet efficient, making it easy to understand while effectively generating a plant watering schedule. It primarily relies on for-loops to iterate through each plant, checking its watering frequency. If a plant’s watering frequency is greater than 0, the program will decrement this value by 1 and move on to the next plant. This continues until a plant’s frequency reaches 0 or less, at which point "WATER NOW" is written next to the plant's name in the external file.

To check for a frequency of 0 is straightforward, but checking for values less than 0 helps handle cases where a plant’s frequency hits 0 on a Saturday. Since watering is skipped on weekends, the frequency would be -1 by Sunday. This allows the plant to be watered on Monday, and using the condition <= 0 also prevents potential bugs in case a frequency unexpectedly drops below -1.

The second loop applies this watering check for each weekday, except on Saturdays and Sundays. On weekends, no watering occurs, and the message "Enjoy your weekend!" is shown instead.

The outermost loop repeats this process 12 times to create a schedule for 12 weeks.

The program has two functions:

- Finding the Next Monday: The function get_next_monday() is essential as it determines the starting point for the schedule, which begins on the next Monday. Using Python’s datetime library, it calculates the upcoming Monday based on today’s date.

- Creating the Schedule: The main schedule() function uses get_next_monday() to set the first date in the plan. From there, it iterates through each day for the next 12 weeks, adjusting plant watering frequencies and marking weekends as non-watering days. Each date is formatted and logged in the schedule.

## How to run:

To run the program, simply execute the Python file named plant-watering-system.py. It will complete without outputting anything in the command line. Once the program has finished, close it and open the plan.txt file, which will now contain the entire schedule.

## Requirements:

- The user should easily view which plants need watering on which date(s).
- The schedule begins on the upcoming Monday and extends for 12 weeks.
- No watering takes place on weekends (Saturdays and Sundays).
- Each plant is watered according to its individual watering frequency, while respecting weekends.

## Future Improvements:

- Improve the layout and display of the watering schedule, for example, by using an interface which shows a water droplet icon when needing water.
- Add watering limit tracker where the plant caretaker can only water a maximum of three plants per day.
