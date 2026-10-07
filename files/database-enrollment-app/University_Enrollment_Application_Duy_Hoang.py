import sqlite3

from pathlib import Path
DB_NAME = str(Path(__file__).with_name("University_Enrollment_Database_Duy_Hoang.db"))


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        sid INTEGER PRIMARY KEY,
        sname TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        cid INTEGER PRIMARY KEY,
        cname TEXT NOT NULL,
        credits INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        sid INTEGER,
        cid INTEGER,
        PRIMARY KEY (sid, cid),
        FOREIGN KEY (sid) REFERENCES students(sid),
        FOREIGN KEY (cid) REFERENCES courses(cid)
    )
    """)

    conn.commit()


def insert_sample_data(conn):
    cursor = conn.cursor()

    students = [
        (1001, "Alice Johnson"),
        (1002, "Bob Smith"),
        (1003, "Charlie Brown"),
        (1004, "Diana Lee"),
        (1005, "Ethan Davis")
    ]

    courses = [
        (2001, "Database Systems", 3),
        (2002, "Psychology 101", 3),
        (2003, "Calculus II", 4),
        (2004, "Cybersecurity Fundamentals", 3),
        (2005, "World History", 3)
    ]

    enrollments = [
        (1001, 2001),
        (1001, 2003),
        (1001, 2002),
        (1002, 2004),
        (1003, 2003),
        (1003, 2005),
        (1003, 2001),
        (1004, 2002),
        (1004, 2004),
        (1005, 2005),
        (1005, 2004),
        (1005, 2003),
        (1005, 2002),
        (1005, 2001)
    ]

    cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?)", students)
    cursor.executemany("INSERT OR IGNORE INTO courses VALUES (?, ?, ?)", courses)
    cursor.executemany("INSERT OR IGNORE INTO enrollments VALUES (?, ?)", enrollments)

    conn.commit()


def get_number(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Invalid response. Please use the correct input.")


def show_students(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.sid, students.sname, COUNT(enrollments.cid)
        FROM students
        LEFT JOIN enrollments ON students.sid = enrollments.sid
        GROUP BY students.sid, students.sname
        ORDER BY students.sid
    """)

    rows = cursor.fetchall()

    print("\n--- ALL STUDENTS ---")
    print("Student ID | Name                 | # of Classes")
    print("------------------------------------------------")

    for row in rows:
        print(f"{row[0]:<10} | {row[1]:<20} | {row[2]}")


def list_courses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses ORDER BY cid")
    rows = cursor.fetchall()

    print("\n--- ALL COURSES ---")
    print("Course ID | Course Name                 | Credits")
    print("------------------------------------------------")

    for row in rows:
        print(f"{row[0]:<9} | {row[1]:<27} | {row[2]}")


def get_or_create_student(conn):
    cursor = conn.cursor()

    while True:
        show_students(conn)

        sid = get_number("\nEnter student ID (-1 for new student): ")

        if sid == -1:
            while True:
                new_sid = get_number("Enter new student ID: ")

                cursor.execute("SELECT * FROM students WHERE sid = ?", (new_sid,))
                if cursor.fetchone():
                    print("Invalid response. That student ID already exists.")
                    continue

                name = input("Enter student name: ").strip()

                if name == "":
                    print("Invalid response. Please use the correct input.")
                    continue

                cursor.execute(
                    "INSERT INTO students (sid, sname) VALUES (?, ?)",
                    (new_sid, name)
                )
                conn.commit()

                print("New student created.")
                return new_sid

        cursor.execute("SELECT * FROM students WHERE sid = ?", (sid,))
        student = cursor.fetchone()

        if student:
            print(f"Welcome, {student[1]}")
            return sid
        else:
            print("Invalid response. Student ID not found.")


def enroll_in_course(conn, sid):
    cursor = conn.cursor()

    list_courses(conn)
    cid = get_number("\nEnter course ID to enroll: ")

    cursor.execute("SELECT * FROM courses WHERE cid = ?", (cid,))
    if not cursor.fetchone():
        print("Invalid response. Course ID not found.")
        return

    cursor.execute("SELECT * FROM enrollments WHERE sid = ? AND cid = ?", (sid, cid))
    if cursor.fetchone():
        print("Invalid response. Already enrolled in that course.")
        return

    cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (sid, cid))
    conn.commit()

    print("Enrollment successful.")
    my_classes(conn, sid)


def withdraw_from_course(conn, sid):
    cursor = conn.cursor()

    my_classes(conn, sid)
    cid = get_number("\nEnter course ID to withdraw: ")

    cursor.execute("SELECT * FROM enrollments WHERE sid = ? AND cid = ?", (sid, cid))
    if not cursor.fetchone():
        print("Invalid response. You are not enrolled in that course.")
        return

    cursor.execute("DELETE FROM enrollments WHERE sid = ? AND cid = ?", (sid, cid))
    conn.commit()

    print("Withdrawal successful.")
    my_classes(conn, sid)


def delete_student(conn, active_sid):
    cursor = conn.cursor()

    show_students(conn)
    sid = get_number("\nEnter student ID to delete: ")

    cursor.execute("SELECT * FROM students WHERE sid = ?", (sid,))
    student = cursor.fetchone()

    if not student:
        print("Invalid response. Student ID not found.")
        return active_sid

    print(f"\nYou selected: {student[1]} (ID: {student[0]})")

    while True:
        confirm = input("Are you sure you want to delete this student? (Y/N): ").strip().upper()

        if confirm == "Y":
            cursor.execute("DELETE FROM enrollments WHERE sid = ?", (sid,))
            cursor.execute("DELETE FROM students WHERE sid = ?", (sid,))
            conn.commit()

            print("Student deleted successfully.")
            show_students(conn)

            if sid == active_sid:
                print("You deleted the active student. Please log in again.")
                return get_or_create_student(conn)

            return active_sid

        elif confirm == "N":
            print("Delete cancelled.")
            return active_sid

        else:
            print("Invalid response. Please use Y or N.")


def search_courses(conn):
    cursor = conn.cursor()

    keyword = input("Enter course name keyword: ").strip()

    if keyword == "":
        print("Invalid response. Please use the correct input.")
        return

    cursor.execute(
        "SELECT * FROM courses WHERE cname LIKE ? ORDER BY cid",
        ('%' + keyword + '%',)
    )

    rows = cursor.fetchall()

    if rows:
        print("\n--- SEARCH RESULTS ---")
        print("Course ID | Course Name                 | Credits")
        print("------------------------------------------------")
        for row in rows:
            print(f"{row[0]:<9} | {row[1]:<27} | {row[2]}")
    else:
        print("No matching courses found.")


def my_classes(conn, sid):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT courses.cid, courses.cname, courses.credits
        FROM courses
        JOIN enrollments ON courses.cid = enrollments.cid
        WHERE enrollments.sid = ?
        ORDER BY courses.cid
    """, (sid,))

    rows = cursor.fetchall()

    print("\n--- MY CLASSES ---")

    if rows:
        print("Course ID | Course Name                 | Credits")
        print("------------------------------------------------")
        for row in rows:
            print(f"{row[0]:<9} | {row[1]:<27} | {row[2]}")
    else:
        print("No enrolled classes.")


def main_menu(conn, sid):
    while True:
        print("\n--- MAIN MENU ---")
        print("L - List Courses")
        print("E - Enroll")
        print("W - Withdraw")
        print("S - Search Courses")
        print("M - My Classes")
        print("A - All Students")
        print("D - Delete Student")
        print("X - Exit")

        choice = input("Choose option: ").strip().upper()

        if choice == "L":
            list_courses(conn)
        elif choice == "E":
            enroll_in_course(conn, sid)
        elif choice == "W":
            withdraw_from_course(conn, sid)
        elif choice == "S":
            search_courses(conn)
        elif choice == "M":
            my_classes(conn, sid)
        elif choice == "A":
            show_students(conn)
        elif choice == "D":
            sid = delete_student(conn, sid)
        elif choice == "X":
            print("Goodbye.")
            break
        else:
            print("Invalid response. Please use L, E, W, S, M, A, D, or X.")


def main():
    conn = create_connection()
    create_tables(conn)
    insert_sample_data(conn)

    sid = get_or_create_student(conn)
    main_menu(conn, sid)

    conn.close()


if __name__ == "__main__":
    main()