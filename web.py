import streamlit as fred
import Keep_functions

todo = Keep_functions.get_todo()


def add():
    box_item = fred.session_state["new_todo"] + "\n"
    todo.append(box_item)
    Keep_functions.write_todo(todo)


fred.title("My Todo App")
fred.subheader("Please do well to follow your todo list")
fred.write("This is going to increase your productivity")

for index, items in enumerate(todo):
    checkedBox = fred.checkbox(items, key=items)
    if checkedBox:
        todo.pop(index)
        Keep_functions.write_todo(todo)
        del fred.session_state[items]
        fred.rerun()


fred.text_input(label=" ", placeholder="Add a todo...", on_change=add, key="new_todo")

# notes="[we use streamlit for web app creation and integrate well with graphs
# session_state create a dictionary with the key in the text_input
# and what we entered in the box is the value, so we assign this value to box_item and append it to our to_do
# to implement complete,we want to check box to delete the box checked
# so we assign a key to session_state, since our complete key works with indexes we use
# the enumerate function to number our to_do,so when we check a box,the session_state
# will assign it to true and with the help of the enumerate function we will get the index of the checked box
# of which we will pop it out from our to_do"


