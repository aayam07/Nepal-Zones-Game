import turtle
import pandas

CHANCES = 14  # Global Constant

screen = turtle.Screen()
screen.setup(width=1300, height=600)
map_of_nepal = "./map_of_nepal_outline.gif"
screen.addshape(map_of_nepal)
turtle.shape(map_of_nepal)  # to display map of nepal onto our screen


def get_missing_zones(map_zones, user_zones):
    missed_zones = [zone for zone in map_zones if zone not in user_zones]  # Conditional List Comprehension
    # Converting missed_zones list to a dataframe
    missed_zones_df = pandas.DataFrame(missed_zones)
    missed_zones_df.to_csv("./zones_to_learn.csv")


# Converting .csv to dataframe using pandas
data = pandas.read_csv("./zones_cordinates.csv")
all_zones = data["zones"].to_list()  # converting zones series to a list of all the zones


score = 0
guessed_zones = []
while CHANCES > 0:
    answer_zone = screen.textinput(title=f"{score}/14 Zones Guessed",
                                   prompt=f"Guess another zone ({CHANCES} guesses left)\n"
                                          f"[Type 'exit' if you want to see the missing zones which "
                                          f"will be given is zones_to_learn.csv file]").title()

    if answer_zone == "Exit":
        get_missing_zones(map_zones=all_zones, user_zones=guessed_zones)
        break

    # checking user guess in our csv file's zones list
    if answer_zone in all_zones:
        matched_row = data[data["zones"] == answer_zone]  # extracts the row form dataframe
        x_cor = int(matched_row.x)
        y_cor = int(matched_row.y)
        tim = turtle.Turtle()  # tim is a turtle object
        tim.penup()
        tim.hideturtle()
        tim.goto(x_cor, y_cor)
        tim.write(answer_zone)  # alternatively, tim.write(matched_row.zones.item())
        score += 1
        if answer_zone not in guessed_zones:
            guessed_zones.append(answer_zone)

    CHANCES -= 1

screen.exitonclick()
