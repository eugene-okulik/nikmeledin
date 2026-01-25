INSERT INTO students (first_name, last_name) VALUES ('Иван', 'Петров');

INSERT INTO books (title, author) VALUES
('Мастер и Маргарита', 'Михаил Булгаков'),
('Преступление и наказание', 'Фёдор Достоевский'),
('Python для начинающих', 'Пол Бэрри');


INSERT INTO book_loans (book_id, student_id, loan_date) VALUES
(1, 1, CURDATE()),
(2, 1, CURDATE()),
(3, 1, CURDATE());


INSERT INTO `groups` (name) VALUES ('ПМИ-21');
UPDATE students SET group_id = 1 WHERE id = 1;


INSERT INTO subjects (name) VALUES
('Математика'),
('Программирование'),
('Базы данных');


INSERT INTO lessons (subject_id, topic, lesson_date) VALUES
(1, 'Тема 1', CURDATE()),
(1, 'Тема 2', DATE_ADD(CURDATE(), INTERVAL 7 DAY)),
(2, 'Тема 1', CURDATE()),
(2, 'Тема 2', DATE_ADD(CURDATE(), INTERVAL 7 DAY)),
(3, 'Тема 1', CURDATE()),
(3, 'Тема 2', DATE_ADD(CURDATE(), INTERVAL 7 DAY));


INSERT INTO marks (student_id, lesson_id, mark) VALUES
(1, 1, 4),
(1, 2, 5),
(1, 3, 4),
(1, 4, 3),
(1, 5, 5),
(1, 6, 4);


SELECT s.name as subject, l.topic, m.mark, l.lesson_date
FROM marks m
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s ON l.subject_id = s.id
WHERE m.student_id = 1
ORDER BY l.lesson_date;


SELECT b.title, b.author, bl.loan_date
FROM book_loans bl
JOIN books b ON bl.book_id = b.id
WHERE bl.student_id = 1 AND bl.return_date IS NULL;


SELECT
    stu.first_name,
    stu.last_name,
    g.name as group_name,
    b.title as book_title,
    b.author as book_author,
    subj.name as subject_name,
    l.topic as lesson_topic,
    m.mark
FROM students stu
LEFT JOIN `groups` g ON stu.group_id = g.id
LEFT JOIN book_loans bl ON stu.id = bl.student_id AND bl.return_date IS NULL
LEFT JOIN books b ON bl.book_id = b.id
LEFT JOIN marks m ON stu.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects subj ON l.subject_id = subj.id
WHERE stu.id = 1;