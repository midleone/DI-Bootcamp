#ex2
import  json
json_file = "sample.json"

with open(json_file, 'r') as file_obj:
    sample = json.load(file_obj)

sample['company']["employee"]["payable"]['salary']

salary = sample['company']["employee"]["payable"]['salary']
print(salary)

with open(json_file, 'r') as file_obj:
       data = json.load(file_obj)

data["company"]["employee"]["birth_date"] = "1999-05-13"

sample_data = json.dumps(data, indent=2)

print(sample_data)

output_sapmle = "output.json"
with open(output_sapmle, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Modified JSON saved to '{output_sapmle}'.")

