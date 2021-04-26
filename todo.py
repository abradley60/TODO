from pathlib import Path
from typing import Optional
import time
import typer
import pandas as pd

app = typer.Typer()


@app.command()
def create(description):
    """creates an item in the todo list

    Args:
        description ([str]): description of the todo item

    """

    df = pd.read_csv("todolist.csv")  # .set_index("id")
    todo_item = {
        "id": str(time.time()).replace(".", ""),
        "description": description,
        "completed": False,
    }
    df = df.append(todo_item, ignore_index=True).set_index("id")
    df.to_csv("todolist.csv")
    return


@app.command()
def list(complete: Optional[bool] = False, no_complete: Optional[bool] = False, substring: Optional[str] = False):
    """print the todo list items

    Args:
        complete (Optional[bool], optional): list only complete items. Defaults to False.
        no_complete (Optional[bool], optional): list only non-complete items. Defaults to False.
        substring (Optional[str], optional): list only items containing string. Defaults to False.
    """
    df = pd.read_csv("todolist.csv").set_index("id")
    if complete:
        df = df[df["completed"] == True]
    if no_complete:
        df = df[df["completed"] == False]
    if substring:
        df = df[df["description"].str.contains(substring)]
    if df.empty:
        print("no todo items to show")
    else:
        print(df)


@app.command()
def update(id_):
    """update the status of a todo item specified by id. If item not complete,
        it will be changed to complete. If item complete, it will be changed to 
        not complete

    Args:
        id_ ([str]): id of the todo list item to upate
    """
    df = pd.read_csv("todolist.csv").set_index("id")
    try:
        desc = df.loc[int(id_)]["description"]
        if df.loc[int(id_)]["completed"]:
            df.loc[int(id_), "completed"] = 0
            print(f"The following task has been changed to uncompleted: {desc}")
        else:
            df.loc[int(id_), "completed"] = 1
            print(f"Congrats on completing the following task!: {desc}")
    except:
        print(f"The specified id is not in list: {id_}")
        print("use list-all command to see items in list")
    df.to_csv("todolist.csv")


@app.command()
def toggle(id_, new_desc):
    df = pd.read_csv("todolist.csv").set_index("id")
    try:
        old_desc = df.loc[int(id_)]["description"]
        df.loc[int(id_), "description"] = "hello"
        print(f"old description: {old_desc}\tnew description: {new_desc}")
    except:
        print(f"The specified id is not in list: {id_}")
        print("use list-all command to see items in list")
    df.to_csv("todolist.csv")


@app.command()
def delete(id_):
    df = pd.read_csv("todolist.csv").set_index("id")
    try:
        df = df.drop(int(id_), axis="index")
        print(f"deleting todo item with description: {df.loc[int(id_)]['description']}")
    except:
        print(f"The specified id is not in list: {id_}")
        print("use list-all to see items in list")
    df.to_csv("todolist.csv")


if __name__ == "__main__":
    app()
