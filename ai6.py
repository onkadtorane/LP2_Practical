def get_score(category):
    while True:
        try:
            print(f"\nRate {category} (0: Poor, 1: Average, 2: Good, 3: Excellent)")
            score = int(input("Enter score: "))
            if score in [0, 1, 2, 3]:
                return score
            else:
                print("⚠️  Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
            print("⚠️  Please enter a valid number.")


def evaluate_performance(total_score):
    if total_score >= 13:
        return "Excellent"
    elif total_score >= 10:
        return "Good"
    elif total_score >= 6:
        return "Average"
    else:
        return "Poor"


def main():
    print("🔍 Employee Performance Evaluation System")
    print("Please rate the employee on the following criteria:")

    punctuality = get_score("Punctuality")
    task_completion = get_score("Task Completion")
    teamwork = get_score("Teamwork")
    innovation = get_score("Innovation")
    leadership = get_score("Leadership")

    total_score = punctuality + task_completion + teamwork + innovation + leadership

    print("\n✅ Evaluation Complete.")
    print(f"Total Score: {total_score}/15")

    performance = evaluate_performance(total_score)
    print(f"🎯 Final Evaluation: {performance}")

    # Optional alert-like message
    if performance == "Excellent":
        print("🌟 Outstanding performance! Consider for promotion.")
    elif performance == "Poor":
        print("⚠️  Needs improvement. Consider training or mentoring.")

if __name__ == "__main__":
    main()
