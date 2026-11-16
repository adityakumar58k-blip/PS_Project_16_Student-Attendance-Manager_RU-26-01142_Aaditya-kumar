print("==============================")
print("     Attendance_Manager")
print("==============================")

FILE_NAME = "attendance.txt"
MIN_PERCENT = 75.0

students = []  # list of dicts: {"roll", "name", "held", "attended"}


# ---------------- File handling ----------------
def load_data():

    students.clear()
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 4:
                    continue  # skip blank or damaged lines
                try:
                    students.append({
                        "roll": int(parts[0]),
                        "name": parts[1],
                        "held": int(parts[2]),
                        "attended": int(parts[3]),
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        pass


def save_data():
    #Save all students to the file (called after every change).
    with open(FILE_NAME, "w") as f:
        for s in students:
            f.write(f"{s['roll']}|{s['name']}|{s['held']}|{s['attended']}\n")


# ---------------- Helpers ----------------
def find_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def read_roll(prompt="Roll: "):
    #ead a roll number; return None if it is not a whole number.
    text = input(prompt).strip()
    if not text.isdigit():
        print("Invalid roll number. Enter digits only.")
        return None
    return int(text)


def percentage(student):
    #Attendance percentage; returns None when no classes are held (avoids divide by zero).
    if student["held"] == 0:
        return None
    return student["attended"] / student["held"] * 100


# ---------------- Features ----------------
def add_student():
    roll = read_roll()
    if roll is None:
        return
    if find_student(roll) is not None:
        print(f"Roll number {roll} already exists.")
        return
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    s = {"roll": roll, "name": name, "held": 0, "attended": 0}
    students.append(s)
    save_data()
    print(f"Student added: {roll} | {name} | Held: 0 | Attended: 0")


def mark_attendance():
    roll = read_roll()
    if roll is None:
        return
    s = find_student(roll)
    if s is None:
        print(f"Roll number {roll} not found.")
        return
    status = input("Status (P/A): ").strip().upper()
    if status not in ("P", "A"):
        print("Invalid status. Enter P or A.")
        return
    s["held"] += 1
    if status == "P":
        s["attended"] += 1
    save_data()
    word = "Present" if status == "P" else "Absent"
    print(f"Marked {word}: {s['roll']} | {s['name']} | "
          f"Held: {s['held']} | Attended: {s['attended']}")


def show_percentage():
    roll = read_roll()
    if roll is None:
        return
    s = find_student(roll)
    if s is None:
        print(f"Roll number {roll} not found.")
        return
    pct = percentage(s)
    if pct is None:
        print(f"{s['name']}: Attendance 0.00% (no classes held yet)")
    else:
        print(f"{s['name']}: Attendance {pct:.2f}%")


def show_shortage_list():
    if not students:
        print("No students found.")
        return
    below = []
    meets = []
    for s in students:
        pct = percentage(s)
        if pct is None:
            continue  # no classes held yet, nothing to judge
        if pct < MIN_PERCENT:
            below.append((s, pct))
        else:
            meets.append((s, pct))

    if below:
        for s, pct in below:
            print(f"Below {MIN_PERCENT:.0f}%: {s['roll']} | {s['name']} | {pct:.2f}%")
    else:
        print(f"No students below {MIN_PERCENT:.0f}%.")
    for s, pct in meets:
        print(f"{s['name']} ({pct:.2f}%) meets the requirement.")


# ---------------- Menu ----------------
def show_menu():
    print("\n===== Student Attendance Manager =====")
    print("1. Add student")
    print("2. Mark attendance")
    print("3. Show attendance percentage")
    print("4. Shortage list (below 75%)")
    print("5. Exit")


def main():
    load_data()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            show_percentage()
        elif choice == "4":
            show_shortage_list()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()
