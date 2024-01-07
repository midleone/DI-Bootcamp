import faker

import faker
fake = faker()
random_data = []
for _ in range(100):
    name = fake.name()
    address = fake.address()
    email = fake.email()
    random_data.append({
        'name': name,
        'address': address,
        'email': email
    })

for data in random_data:
    print(f"Name: {data['name']}\nAddress: {data['address']}\nEmail: {data['email']}\n")