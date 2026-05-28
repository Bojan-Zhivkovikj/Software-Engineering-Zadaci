import logging
# STAYS SAME: logging is used to save errors and program activity


logging.basicConfig(
    filename="function_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# STAYS SAME: logging configuration
# MIGHT CHANGE: filename can change


def divide_numbers(num1, num2):
    # MIGHT CHANGE: function name and operation

    return num1 / num2
    # MIGHT CHANGE: risky operation
    # POSSIBLE ERROR: ZeroDivisionError


def access_list(my_list, index):
    # MIGHT CHANGE: function name and list

    return my_list[index]
    # MIGHT CHANGE: index value
    # POSSIBLE ERROR: IndexError


def access_dictionary(student):
    # MIGHT CHANGE: dictionary name and key

    return student["grade"]
    # MIGHT CHANGE: key name
    # POSSIBLE ERROR: KeyError


def string_operation():
    # MIGHT CHANGE: string operation

    text = "hello"
    # MIGHT CHANGE: string value

    return text[20]
    # MIGHT CHANGE: index value
    # POSSIBLE ERROR: IndexError


def wrong_type_operation():
    # MIGHT CHANGE: operation/data types

    return "5" + 5
    # POSSIBLE ERROR: TypeError


while True:
    # STAYS SAME: loop allows retry after errors

    try:
        # STAYS SAME STRUCTURE: risky function calls go inside try

        logging.debug("New execution started.")
        # STAYS SAME: log start of attempt

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        # MIGHT CHANGE: input values/prompts
        # POSSIBLE ERROR: ValueError

        result = divide_numbers(num1, num2)
        # MIGHT CHANGE: function being called
        # POSSIBLE ERROR: ZeroDivisionError

        print("Division Result:", result)

        numbers = [10, 20, 30]
        # MIGHT CHANGE: list values

        print(access_list(numbers, 1))
        # MIGHT CHANGE: index
        # POSSIBLE ERROR: IndexError

        student = {
            "name": "Bojan"
        }
        # MIGHT CHANGE: dictionary data

        print(access_dictionary(student))
        # MIGHT CHANGE: dictionary/key
        # POSSIBLE ERROR: KeyError

        print(string_operation())
        # MIGHT CHANGE: function logic
        # POSSIBLE ERROR: IndexError

        print(wrong_type_operation())
        # MIGHT CHANGE: function logic
        # POSSIBLE ERROR: TypeError


    except ValueError as error:
        # STAYS SAME TEMPLATE: handles invalid number conversion

        logging.error(error)
        print("ValueError:", error)


    except ZeroDivisionError as error:
        # STAYS SAME TEMPLATE: handles division by zero

        logging.error(error)
        print("ZeroDivisionError:", error)


    except IndexError as error:
        # STAYS SAME TEMPLATE: handles invalid list/string index

        logging.error(error)
        print("IndexError:", error)


    except KeyError as error:
        # STAYS SAME TEMPLATE: handles missing dictionary key

        logging.error(error)
        print("KeyError:", error)


    except TypeError as error:
        # STAYS SAME TEMPLATE: handles wrong data types

        logging.error(error)
        print("TypeError:", error)


    except Exception as error:
        # STAYS SAME TEMPLATE: final backup
        # IMPORTANT: must always stay last

        logging.critical(error)
        print("Unexpected Error:", error)


    else:
        # STAYS SAME: runs only if no error happened

        logging.info("Program executed successfully.")
        print("All functions executed successfully.")

        break
        # STAYS SAME: stops loop after successful run


    finally:
        # STAYS SAME: always runs

        logging.debug("Execution attempt finished.")
        print("End of attempt.")


# =====================================================
# EXAM NOTES
# =====================================================

# STAYS SAME:
# - import logging
# - logging.basicConfig(...)
# - while True
# - try
# - except specific error
# - except Exception as error LAST
# - else
# - finally

# MIGHT CHANGE:
# - function names
# - function parameters
# - risky operations
# - input prompts
# - printed messages
# - log file name

# BEST STRUCTURE:
# 1. Put risky code inside functions.
# 2. Call the functions inside try.
# 3. Catch expected errors with specific except blocks.
# 4. Put except Exception as error last.
# 5. Use else for successful execution.
# 6. Use finally for code that must always run.