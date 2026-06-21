def generate_job_description(role, skills, experience):
    return (
        f"We are hiring a {role} with {experience} years of experience. "
        f"The ideal candidate should have skills in {skills}. "
        f"The role involves teamwork, problem-solving, and continuous learning."
    )


def screen_resume(candidate_name, candidate_skills, required_skills):
    candidate_set = {skill.strip().lower() for skill in candidate_skills.split(",")}
    required_set = {skill.strip().lower() for skill in required_skills.split(",")}

    matched_skills = candidate_set.intersection(required_set)

    if matched_skills:
        result = "Selected"
    else:
        result = "Needs Review"

    return (
        f"Candidate: {candidate_name}\n"
        f"Matched Skills: {', '.join(matched_skills) if matched_skills else 'None'}\n"
        f"Screening Result: {result}"
    )


def generate_interview_questions(role):
    return [
        f"What interests you about the {role} position?",
        "Explain a challenging project you worked on.",
        "How do you handle deadlines and pressure?",
        "Describe a situation where you solved a technical problem.",
        "Where do you see yourself in 5 years?"
    ]