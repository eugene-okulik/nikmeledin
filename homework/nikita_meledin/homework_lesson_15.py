import mysql.connector as mysql
import random
from datetime import date

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


cursor.execute("INSERT INTO students (first_name, last_name) VALUES (%s, %s)", ('Иван', 'Петров'))
student_id = cursor.lastrowid


books = [('Мастер и Маргарита', 'Михаил Булгаков'),
         ('Преступление и наказание', 'Фёдор Достоевский'),
         ('Python для начинающих', 'Пол Бэрри')]
cursor.executemany("INSERT INTO books (title, author) VALUES (%s, %s)", books)


cursor.execute("SELECT LAST_INSERT_ID() as first_id")
first_book_id = cursor.fetchone()['first_id']
book_loans = [(first_book_id + i, student_id, date.today()) for i in range(len(books))]
cursor.executemany("INSERT INTO book_loans (book_id, student_id, loan_date) VALUES (%s, %s, %s)", book_loans)


cursor.execute("INSERT INTO `groups` (name) VALUES (%s)", ('ПМИ-21',))
group_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))


subjects = ['Математика', 'Программирование', 'Базы данных']
subject_ids = []
for subject in subjects:
    cursor.execute("INSERT INTO subjects (name) VALUES (%s)", (subject,))
    subject_ids.append(cursor.lastrowid)


lesson_ids = []
for subject_id in subject_ids:
    for i in range(2):
        cursor.execute(
            "INSERT INTO lessons (subject_id, topic, lesson_date) VALUES (%s, %s, %s)",
            (subject_id, f'Занятие {i+1}', date.today())
        )
        lesson_ids.append(cursor.lastrowid)


marks = [(student_id, lesson_id, random.randint(3, 5)) for lesson_id in lesson_ids]
cursor.executemany("INSERT INTO marks (student_id, lesson_id, mark) VALUES (%s, %s, %s)", marks)

db.commit()


cursor.execute("""
    SELECT m.mark, l.topic, s.name
    FROM marks m
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s ON l.subject_id = s.id
    WHERE m.student_id = %s
""", (student_id,))
print("Все оценки студента:")
for row in cursor.fetchall():
    print(f"{row['name']}: {row['topic']} - {row['mark']}")

cursor.execute("""
    SELECT b.title, b.author
    FROM book_loans bl
    JOIN books b ON bl.book_id = b.id
    WHERE bl.student_id = %s AND bl.return_date IS NULL
""", (student_id,))
print("\nКниги у студента:")
for row in cursor.fetchall():
    print(f"'{row['title']}' - {row['author']}")

cursor.execute("""
    SELECT s.first_name, s.last_name, g.name as group_name, b.title as book_title,
           subj.name as subject_name, m.mark
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN book_loans bl ON s.id = bl.student_id AND bl.return_date IS NULL
    LEFT JOIN books b ON bl.book_id = b.id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects subj ON l.subject_id = subj.id
    WHERE s.id = %s
""", (student_id,))

print("\nВся информация о студенте:")
for row in cursor.fetchall():
    print(f"{row['first_name']} {row['last_name']} | Группа: {row['group_name']} | "
          f"Книга: {row['book_title'] or 'нет'} | Предмет: {row['subject_name'] or 'нет'} | "
          f"Оценка: {row['mark'] or 'нет'}")

cursor.close()
db.close()
