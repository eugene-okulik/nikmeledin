import csv
import os
from connection import connect


connection = connect()
if not connection:
    exit()


current_folder = os.path.dirname(__file__)
project_folder = os.path.dirname(os.path.dirname(os.path.dirname(current_folder)))
file_path = os.path.join(project_folder, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


csv_data = []
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row:
            csv_data.append({
                'book': row[0],
                'student': row[1],
                'group': row[2]
            })

print(f"Прочитали {len(csv_data)} строк из CSV")


cursor = connection.cursor()
not_found = []

for item in csv_data:
    query = """
        SELECT * FROM books b
        JOIN students s ON b.taken_by_student_id = s.id
        JOIN `groups` g ON s.group_id = g.id
        WHERE b.title = %s AND s.name = %s AND g.title = %s
    """
    cursor.execute(query, (item['book'], item['student'], item['group']))
    result = cursor.fetchone()

    if result:
        print(f"Есть в БД: {item['book']} - {item['student']} - {item['group']}")
    else:
        print(f"Нет в БД: {item['book']} - {item['student']} - {item['group']}")
        not_found.append(item)


print("\n" + "=" * 40)
if not_found:
    print("Чего нет в БД:")
    for item in not_found:
        print(f"  - {item['book']} (ученик: {item['student']}, группа: {item['group']})")
else:
    print("Все данные из CSV есть в БД!")

cursor.close()
connection.close()
