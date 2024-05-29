
from helpers import (
    exit_program,
    list_makes,
    find_make_by_name,
    find_make_by_id,
    create_make,
    update_make,
    delete_make,
    list_models,
    find_model_by_name,
    find_model_by_id,
    create_model,
    update_model,
    delete_model,
    list_make_models
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_makes()
        elif choice == "2":
            find_make_by_name()
        elif choice == "3":
            find_make_by_id()
        elif choice == "4":
            create_make()
        elif choice == "5":
            update_make()
        elif choice == "6":
            delete_make()
        elif choice == "7":
            list_models()
        elif choice == "8":
            find_model_by_name()
        elif choice == "9":
            find_model_by_id()
        elif choice == "10":
            create_model()
        elif choice == "11":
            update_model()
        elif choice == "12":
            delete_model()
        elif choice == "13":
            list_make_models()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all makes")
    print("2. Find make by name")
    print("3. Find make by id")
    print("4: Create make")
    print("5: Update make")
    print("6: Delete make")
    print("7. List all models")
    print("8. Find model by name")
    print("9. Find model by id")
    print("10: Create model")
    print("11: Update model")
    print("12: Delete model")
    print("13: List all models in a make")


if __name__ == "__main__":
    main()
