import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=1300, height=600)
map_of_nepal = "./map_of_nepal_outline.gif"
screen.addshape(map_of_nepal)
turtle.shape(map_of_nepal)  # to display map of nepal onto our screen

# This part is to get the screen coordinates of all the zones
# for our .csv file.

# def get_screen_cor(x, y):
#     with open("./screen_cordinates.txt", mode="a") as file:
#         file.write(f"{x, y}")
#
# # Event listeners
# # when screen is clicked by mouse, the clicked position's x,y is passed as
# # argument to the function
# screen.onscreenclick(fun=get_screen_cor)
# turtle.mainloop()


# Converting .csv to dataframe using pandas
data = pandas.read_csv("./zones_cordinates.csv")
all_zones = data["zones"].to_list()  # converting zones series to a list of all the zones
print(all_zones)










# screen.exitonclick()
