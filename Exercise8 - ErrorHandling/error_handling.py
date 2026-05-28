import logging
# STAYS SAME: logging is used to save information/errors into app.log


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# STAYS SAME: logging setup


while True:
    # STAYS SAME: keeps asking until successful input/calculation

    try:
        # =====================================================
        # MAIN RISKY CODE
        # =====================================================
        # MIGHT CHANGE depending on task

        logging.debug("Program started new attempt.")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2

    except ValueError as error:
        logging.error(error)
        print("ValueError:", error)
        print("Error: Please enter valid whole numbers.")

    except ZeroDivisionError as error:
        logging.error(error)
        print("ZeroDivisionError:", error)
        print("Error: Cannot divide by zero.")

    except TypeError as error:
        logging.error(error)
        print("TypeError:", error)
        print("Error: Wrong data type used.")

    except IndexError as error:
        logging.error(error)
        print("IndexError:", error)
        print("Error: List index out of range.")

    except KeyError as error:
        logging.error(error)
        print("KeyError:", error)
        print("Error: Dictionary key not found.")

    except FileNotFoundError as error:
        logging.error(error)
        print("FileNotFoundError:", error)
        print("Error: File not found.")

    except PermissionError as error:
        logging.error(error)
        print("PermissionError:", error)
        print("Error: Permission denied.")

    except AttributeError as error:
        logging.error(error)
        print("AttributeError:", error)
        print("Error: Object does not have this attribute/method.")

    except ImportError as error:
        logging.error(error)
        print("ImportError:", error)
        print("Error: Module/import problem.")

    except NameError as error:
        logging.error(error)
        print("NameError:", error)
        print("Error: Variable/function name is not defined.")

    except OverflowError as error:
        logging.error(error)
        print("OverflowError:", error)
        print("Error: Number is too large.")

    except Exception as error:
        # MUST ALWAYS BE LAST

        logging.critical(error)
        print("Unexpected Error:", error)

    else:
        # RUNS ONLY IF NO ERROR OCCURRED

        logging.info("Program executed successfully.")
        print("Result:", result)
        print("Input verified successfully.")

        break

    finally:
        # ALWAYS RUNS

        logging.debug("One attempt finished.")
        print("End of attempt.")


# =====================================================
# EXAM NOTES: WHICH EXCEPTIONS TO USE
# =====================================================

# GENERAL RULE:
# 1. Put specific exceptions first.
# 2. Put except Exception as error LAST.
# 3. Only include exceptions relevant to the task.
# 4. Logging is optional, but useful for saving error history.


# =====================================================
# NUMBERS / CALCULATOR TASKS
# =====================================================

# Risky code examples:
# int(input())
# float(input())
# num1 / num2
# num1 + num2
#
# Suggested order:
# except ValueError
# except ZeroDivisionError
# except TypeError
# except OverflowError
# except Exception


# =====================================================
# STRING TASKS
# =====================================================

# Risky code examples:
# text[20]
# text.some_wrong_method()
# int(text)
# "5" + 5
#
# Suggested order:
# except IndexError
# except AttributeError
# except ValueError
# except TypeError
# except Exception


# =====================================================
# LIST TASKS
# =====================================================

# Risky code examples:
# my_list[10]
# my_list.remove(value_that_does_not_exist)
# int(my_list[0])
#
# Suggested order:
# except IndexError
# except ValueError
# except TypeError
# except Exception


# =====================================================
# DICTIONARY TASKS
# =====================================================

# Risky code examples:
# student["grade"]
# int(student["age"])
#
# Suggested order:
# except KeyError
# except ValueError
# except TypeError
# except Exception


# =====================================================
# FILE TASKS
# =====================================================

# Risky code examples:
# open("data.txt", "r")
# file.read()
#
# Suggested order:
# except FileNotFoundError
# except PermissionError
# except UnicodeDecodeError
# except Exception


# =====================================================
# IMPORT / MODULE TASKS
# =====================================================

# Risky code examples:
# import wrong_module
# from module import wrong_name
#
# Suggested order:
# except ImportError
# except ModuleNotFoundError
# except Exception


# =====================================================
# VARIABLE / FUNCTION NAME TASKS
# =====================================================

# Risky code examples:
# print(undefined_variable)
# wrong_function()
#
# Suggested order:
# except NameError
# except TypeError
# except Exception


# =====================================================
# UNIVERSAL BACKUP
# =====================================================

# If you are unsure what error can happen:
# use the most obvious specific exceptions first,
# then finish with:
#
# except Exception as error:
#     print("Unexpected Error:", error)
#
# NEVER put except Exception first.