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

# 1. Добавляем студента
cursor.execute(
    "INSERT INTO students (first_name, last_name) VALUES (%s, %s)",
    ('Иван', 'Петров')
)
student_id = cursor.lastrowid
print(f"Добавлен студент с ID: {student_id}")

# 2. Добавляем книги и сразу указываем, кто их взял
books = [
    ('Мастер и Маргарита', 'Михаил Булгаков'),
    ('Преступление и наказание', 'Фёдор Достоевский'),
    ('Python для начинающих', 'Пол Бэрри')
]

# Добавляем книги с указанием student_id в поле taken_by_student_id
books_with_student = []
for title, author in books:
    books_with_student.append((title, author, student_id))

cursor.executemany(
    "INSERT INTO books (title, author, taken_by_student_id) "
    "VALUES (%s, %s, %s)",
    books_with_student
)
print(f"Добавлено {len(books)} книг, все выданы студенту {student_id}")

# 3. Создаем группу и добавляем студента в группу
cursor.execute(
    "INSERT INTO `groups` (name) VALUES (%s)",
    ('ПМИ-21',)
)
group_id = cursor.lastrowid
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
print(f"Студент добавлен в группу ПМИ-21 (ID: {group_id})")

# 4. Добавляем предметы
subjects = ['Математика', 'Программирование', 'Базы данных']
subject_ids = []
for subject in subjects:
    cursor.execute(
        "INSERT INTO subjects (name) VALUES (%s)",
        (subject,)
    )
    subject_ids.append(cursor.lastrowid)
print(f"Добавлены предметы: {', '.join(subjects)}")

# 5. Добавляем уроки (по 2 на каждый предмет)
lesson_ids = []
for subject_id in subject_ids:
    for i in range(2):
        cursor.execute(
            "INSERT INTO lessons (subject_id, topic, lesson_date) "
            "VALUES (%s, %s, %s)",
            (subject_id, f'Занятие {i + 1}', date.today())
        )
        lesson_ids.append(cursor.lastrowid)
print(f"Добавлено {len(lesson_ids)} уроков")

# 6. Добавляем оценки
marks = []
for lesson_id in lesson_ids:
    marks.append((student_id, lesson_id, random.randint(3, 5)))

cursor.executemany(
    "INSERT INTO marks (student_id, lesson_id, mark) "
    "VALUES (%s, %s, %s)",
    marks
)
print(f"Добавлено {len(marks)} оценок")

db.commit()
print("\n=== Все изменения сохранены в БД ===\n")

# 7. Проверяем все оценки студента
cursor.execute(
    """
    SELECT m.mark, l.topic, s.name
    FROM marks m
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s ON l.subject_id = s.id
    WHERE m.student_id = %s
    ORDER BY s.name, l.topic
    """,
    (student_id,)
)
print("Все оценки студента:")
for row in cursor.fetchall():
    print(f"  {row['name']}: {row['topic']} - {row['mark']}")

# 8. Проверяем книги, которые взял студент
cursor.execute(
    """
    SELECT title, author
    FROM books
    WHERE taken_by_student_id = %s
    """,
    (student_id,)
)
print("\nКниги у студента:")
books_taken = cursor.fetchall()
if books_taken:
    for row in books_taken:
        print(f"  '{row['title']}' - {row['author']}")
else:
    print("  У студента нет книг")

# 9. Вся информация о студенте
cursor.execute(
    """
    SELECT
        s.first_name,
        s.last_name,
        g.name as group_name,
        GROUP_CONCAT(
            DISTINCT CONCAT(b.title, ' (', b.author, ')')
            SEPARATOR '; '
        ) as books,
        GROUP_CONCAT(
            DISTINCT CONCAT(subj.name, ': ', m.mark)
            SEPARATOR '; '
        ) as marks_list
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects subj ON l.subject_id = subj.id
    WHERE s.id = %s
    GROUP BY s.id, s.first_name, s.last_name, g.name
    """,
    (student_id,)
)

print("\nВся информация о студенте:")
row = cursor.fetchone()
if row:
    print(f"  {row['first_name']} {row['last_name']}")
    print(f"  Группа: {row['group_name']}")
    print(f"  Книги: {row['books'] or 'нет'}")
    print(f"  Оценки: {row['marks_list'] or 'нет'}")

cursor.close()
db.close()
print("\nСоединение с БД закрыто")
