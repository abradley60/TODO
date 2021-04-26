# Basic Python Command-Line ToDo List

## Operations:
Create - Create an item for the to-do list. e.g. "walk dog"
List - List all the items in the to-do list. Filter by completed or key word (e.g. dog)
Toggle - Update the DESCRIPTION of a to-do item.
Update - Update the STATUS of a to-do item.
Delete - Delete a to-do list item

## Example usage 

python todo.py create "take the dog for a walk"<br />
creates a new todo list item

python todo.py list --no-complete --substring "dog"<br />
return all the non completed items containing the word dog

python todo.py delete "12843364745"<br />
deletes the todo item with the id "12843364745"

## Next steps
- Add ability to create and delete multiple items
- Add unit testing capability
- Add basic UI
- Geneally improve functionality and add 
