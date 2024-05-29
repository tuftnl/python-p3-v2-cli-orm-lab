from models.make import Make
from models.model import Model


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the make functions in this lesson


def list_makes():
    makes = Make.get_all()
    for make in makes:
        print(make)


def find_make_by_name():
    name = input("Enter the make's name: ")
    make = Make.find_by_name(name)
    print(make) if make else print(
        f'Make {name} not found')


def find_make_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the make's id: ")
    make = Make.find_by_id(id_)
    print(make) if make else print(f'Make {id_} not found')


def create_make():
    name = input("Enter the make's name: ")
    location = input("Enter the make's location: ")
    try:
        make = Make.create(name, location)
        print(f'Success: {make}')
    except Exception as exc:
        print("Error creating make: ", exc)


def update_make():
    id_ = input("Enter the make's id: ")
    if make := Make.find_by_id(id_):
        try:
            name = input("Enter the make's new name: ")
            make.name = name
            location = input("Enter the make's new location: ")
            make.location = location

            make.update()
            print(f'Success: {make}')
        except Exception as exc:
            print("Error updating make: ", exc)
    else:
        print(f'Make {id_} not found')


def delete_make():
    id_ = input("Enter the make's id: ")
    if make := Make.find_by_id(id_):
        make.delete()
        print(f'Make {id_} deleted')
    else:
        print(f'Make {id_} not found')


# You'll implement the model functions in the lab

def list_models():
    models = Model.get_all()
    for model in models:
        print(model)


def find_model_by_name():
    name = input("Enter the model's name: ")
    model = Model.find_by_name(name)
    print (model) if model else print (f"Model {name} not found")


def find_model_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the make's id: ")
    model = Model.find_by_id(id_)
    print(model) if model else print(f'Make {id_} not found')


def create_model():
    name = input("Enter the model's name: ")
    form_style = input("Enter the form-type: ")
    color = input("Enter the color of the vehicle:")
    make_id = input("Enter the model's make id: ")
    try:
        model = Model.create(name, form_style, color, int(make_id))
        print(f'Success: {model}')
    except Exception as exc:
        print("Error creating model: ", exc)


def update_model():
    id_ = input("Enter the models's id: ")
    if model := Model.find_by_id(id_):
        try: 
            name = input("Enter the model's new name: ")
            model.name = name
            form_style = input("Enter the new form-type: ")
            model.form_style = form_style
            make_id = input("Enter the new make id: ")
            model.make_id = int(make_id)

            model.update()
            print(f'Success {model}')
        except Exception as exc:
            print("Error updating model", exc)
    else: 
        print(f'Model {id_} not found')


def delete_model():
    id_ = input("Enter the model's id: ")
    if model := Model.find_by_id(id_):
        model.delete()
        print(f'Model {id_} deleted')
    else:
        print(f'Model {id_} not found')


def list_make_models():
    id_ = input("Enter the make's id: ")
    if make := Make.find_by_id(id_):
        try:
            for model in make.models():
                print(model)
        except Exception as exc:
            print("Error listing models", exc)
    else : 
        print(f"Can not find make by id of {id_}")