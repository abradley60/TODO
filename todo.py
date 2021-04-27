from pathlib import Path
from typing import Optional
import time
import typer
import pandas as pd

app = typer.Typer()


@app.command()
def create(description, save: Optional[bool] = True, df: Optional[bool] = False):
    """creates an item in the todo list

    Args:
        description ([str]): description of the todo item

    """
    if not isinstance(df, pd.DataFrame):
        df = pd.read_csv("todolist.csv")  # .set_index("id")
    else:
        df = pd.DataFrame()
    id_ = int(str(time.time()).replace(".", ""))
    todo_item = {
        "id": id_,
        "description": description,
        "completed": False,
    }
    df = df.append(todo_item, ignore_index=True).set_index("id")
    if save:
        df.to_csv("todolist.csv")
    return id_, df


@app.command()
def list(
    complete: Optional[bool] = False,
    no_complete: Optional[bool] = False,
    substring: Optional[str] = False,
    df: Optional[bool] = False,
):
    """print the todo list items

    Args:
        complete (Optional[bool], optional): list only complete items. Defaults to False.
        no_complete (Optional[bool], optional): list only non-complete items. Defaults to False.
        substring (Optional[str], optional): list only items containing string. Defaults to False.
    """
    if not isinstance(df, pd.DataFrame):
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
def update(id_, save: Optional[bool] = True, df: Optional[bool] = False):
    """update the status of a todo item specified by id. If item not complete,
        it will be changed to complete. If item complete, it will be changed to 
        not complete

    Args:
        id_ ([str]): id of the todo list item to upate
    """
    if not isinstance(df, pd.DataFrame):
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
    if save:
        df.to_csv("todolist.csv")
    return df


@app.command()
def toggle(id_, new_desc, save: Optional[bool] = True, df: Optional[bool] = False):
    """Update description of todo item

    Args:
        id_ (str): task id
        new_desc (str): task description
        save (Optional[bool], optional): save the new list. Defaults to True.
        df (Optional[bool], optional): pass in df, else load existing. Defaults to False.

    Returns:
        [type]: [description]
    """
    if not isinstance(df, pd.DataFrame):
        df = pd.read_csv("todolist.csv").set_index("id")
    try:
        old_desc = df.loc[int(id_)]["description"]
        df.loc[int(id_), "description"] = new_desc
        print(f"old description: {old_desc}\tnew description: {new_desc}")
    except:
        print(f"The specified id is not in list: {id_}")
        print("use list-all command to see items in list")
    if save:
        df.to_csv("todolist.csv")
    return df


@app.command()
def delete(id_, save: Optional[bool] = True, df: Optional[bool] = False):
    """Delete task by ID

    Args:
        id_ (str): task id.
        save (Optional[bool], optional): save the new list. Defaults to True.
        df (Optional[bool], optional): pass in df, else load existing. Defaults to False.

    Returns:
        [type]: [description]
    """
    if not isinstance(df, pd.DataFrame):
        df = pd.read_csv("todolist.csv").set_index("id")
    try:
        df = df.drop(int(id_), axis="index")
        print(f"deleting todo item with description: {df.loc[int(id_)]['description']}")
    except:
        print(f"The specified id is not in list: {id_}")
        print("use list-all to see items in list")
    if save:
        df.to_csv("todolist.csv")
    return df


if __name__ == "__main__":
    app()
