import csv

def add_record(date, subject, study_time, comment):
        try:
            with open("study_record.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([date, subject, study_time, comment])
            return True
        except Exception:
            return False

def get_records():
    records = []
    try:
        with open('study_record.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for line in reader:
                if len(line) < 3:
                    continue
                record = {"date": line[0], "subject": line[1], "time": line[2], "comment": line[3] if len(line) >= 4 else ""}
                records.append(record)
        records.sort(key=lambda x:x["date"])
        return records
    except FileNotFoundError:
        return []

def get_average():
    total = 0
    count = 0
    try:
        with open('study_record.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for line in reader:
                try:
                    total += float(line[2])
                    count += 1
                except (ValueError, IndexError):
                    continue

            if count > 0:
                return total / count
            else:
                return None
    except FileNotFoundError:
        return None

def get_total():
    total = 0
    try:
        with open('study_record.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for line in reader:
                try:
                    total += float(line[2])
                except (ValueError, IndexError):
                    continue
            return total
    except FileNotFoundError:
        return None