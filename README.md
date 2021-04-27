# Basic Python Command-Line ToDo List

## Operations:
Create - Create an item for the to-do list. e.g. "walk dog".<br />
List - List all the items in the to-do list. Filter by completed or key word (e.g. dog).<br />
Toggle - Update the DESCRIPTION of a to-do item.<br />
Update - Update the STATUS of a to-do item.<br />
Delete - Delete a to-do list item. <br />

## Example usage / basic docs

python todo.py create "take the dog for a walk"<br />
creates a new todo list item

python todo.py list --no-complete --substring "dog"<br />
return all the non completed items containing the word dog

python todo.py delete "12843364745"<br />
deletes the todo item with the id "12843364745"

python todo.py toggle "12843364745" "take the dog for a run"
updates the description of todo item with id "12843364745"

## Strengths
- Ability to create, update, edit and delete items from a to do list
- The basic functionality required for a todo list
- The use of typer over argparse


## Next steps / Improvements
- Geneally improve functionality and add some FUNK
- Add ability to create and delete multiple items
- Add unit testing
- Complete all function type annotations
- Add basic UI
- Edit / delete items based on description rather than just id

