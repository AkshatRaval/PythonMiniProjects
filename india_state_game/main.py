import turtle as t
import pandas

data = pandas.read_csv("india_state_game/dataofstates.csv")
all_states = data.state.to_list()
    

screen = t.Screen()
screen.title("India Map Game")

correct_states = []
image = "india_state_game/india-outline-maps.gif"
screen.addshape(image)
t.shape(image)
missed_states = []

while len(correct_states) < len(all_states):
    user_input = screen.textinput(title=f"{len(correct_states)}/31 States are Correct", prompt="Enter State Names...").title()
    if user_input == "Exit":
        for state in all_states:
            if state not in correct_states:
                missed_states.append(state)
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv("india_state_game/missing_states.csv")
        break
    if user_input in all_states:
        correct_states.append(user_input)
        state = t.Turtle()
        state.hideturtle()
        state.penup()    
        state_data = data[data.state == user_input]
        state.goto(state_data.x.item(), state_data.y.item())
        state.write(state_data.state.item())
    
screen.mainloop()