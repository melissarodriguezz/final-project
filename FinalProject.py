def read_availability_file(file_path):
   availability_data = {}
   with open(file_path, 'r') as file:
       for line in file:
           user, *availability = line.strip().split(',')
           availability_data[user] = availability
   return availability_data


def calculate_availability(availability_data):
   availability_count = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0}
   for user, availability in availability_data.items():
       for i, status in enumerate(availability):
           if status.lower() == 'yes':
               availability_count[list(availability_count.keys())[i]] += 1
   return availability_count


def color_code_availability(availability_count):
   for day, count in availability_count.items():
       if count > len(availability_count) / 2:
           print(f"{day}: {count} users available \033[92m(green)\033[0m")
       else:
           print(f"{day}: {count} users available \033[91m(red)\033[0m")


file_path = 'availability.txt'
availability_data = read_availability_file(file_path)
availability_count = calculate_availability(availability_data)
color_code_availability(availability_count)
