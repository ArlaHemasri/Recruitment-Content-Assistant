from recruitment_assistant import (
    generate_job_description,
    screen_resume,
    generate_interview_questions
)

def main():
    print("=== Recruitment Content Assistant ===")

    role = input("Enter job role: ")
    skills = input("Enter required skills (comma separated): ")
    experience = input("Enter required experience (years): ")

    job_desc = generate_job_description(role, skills, experience)

    print("\n--- Job Description ---")
    print(job_desc)

    candidate_name = input("\nEnter candidate name: ")
    candidate_skills = input("Enter candidate skills (comma separated): ")

    screening_result = screen_resume(
        candidate_name,
        candidate_skills,
        skills
    )

    print("\n--- Resume Screening Result ---")
    print(screening_result)

    questions = generate_interview_questions(role)

    print("\n--- Interview Questions ---")
    for q in questions:
        print(f"- {q}")

if __name__ == "__main__":
    main()