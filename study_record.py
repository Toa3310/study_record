import csv

def record():
    try: 
        date = input("日付を入力してください(例: 4/1): ")
        subject = input("勉強内容を入力してください(例: 数学): ")
        study_time = float(input("勉強時間を入力してください(単位: 時間): "))
        comment = input("コメント(詳細内容,書かなくてもOK!): ")
        return {"date": date, "subject": subject, "time": study_time, "comment": comment}
    except ValueError:
        print("入力内容に不備がありました")
        return None

mode = input("どのモードで処理しますか？(1: 記録,2: 一覧を見る, 3: 平均をみる): ")
if mode == "1":
    result = record()
    if result is None:
        print("処理を終了します")
    else:
        with open("study_record.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([result["date"], result["subject"], result["time"], result["comment"]])
        print("記録が正常に終了しました")
        print(f"日付: {result['date']}, 内容: {result['subject']}, 勉強時間: {result['time']}時間, コメント: {result['comment']}")
if mode == "2":
    with open('study_record.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        print("\n---記録一覧---")
        for line in reader:
            if len(line) >= 4 and line[3] != "":
                print(f"日付: {line[0]}, 内容: {line[1]}, 勉強時間: {line[2]}時間, コメント: {line[3]}")
            else:
                print(f"日付: {line[0]}, 内容: {line[1]}, 勉強時間: {line[2]}時間, コメント: なし")