import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "us_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# print(guess_state)
data = pandas.read_csv("50_states.csv")
# print(data)

# is_game_on = True

all_states = data["state"].tolist()

# for state in all_states:
#     while is_game_on:
#         if state == guess_state:
#                 # print(state)
#             score += 1
#             print(score)
#             correct_guesses.append(state)
#             state_row = data[data["state"] == state]
#             x_coor = float(state_row.x)
#             y_coor = float(state_row.y)
#             print(x_coor, y_coor)
#             # turtle.goto(x_coor, y_coor)
#             t = turtle.Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(x_coor, y_coor)
#             t.write(state, font=('monaco', 8, 'bold'), align='left')
#         else:
#             is_game_on = False
#
# print(score)
# print(correct_guesses)
#
# # How to get x and y coordinates when user onclick on screen
# # def get_mouse_click_coor(x, y):
# #     # turtle.onscreenclick(None)
# #     print(x, y)
# #
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# turtle.addshape(image)

score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    guess_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct",
                                   prompt="Input another state name").title()
    if guess_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess_state in all_states:
        correct_guesses.append(guess_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == guess_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess_state)

# screen.exitonclick()
# find missing states and store in a csv file



