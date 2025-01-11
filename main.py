from larp_agent import generate_ascii_larp
from helper_module_1 import process_data
from helper_module_2 import validate_input
from helper_module_3 import log_activity
from helper_module_4 import format_output

def main():
    input_data = "Sample Input"
    processed_data = process_data(input_data)
    if validate_input(processed_data):
        log_activity("Input validated")
        result = generate_ascii_larp()
        print(format_output(result))
    else:
        log_activity("Validation failed")
        print("Invalid input")

if __name__ == "__main__":
    main()