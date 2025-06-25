import fitz
import argparse

important_skills = ['Python', 'SQL', 'Machine Learning', 'Data Analysis', 'Pandas', 'TensorFlow']

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print("Error reading PDF:", e)
        return ""

def analyze_resume(text):
    text_lower = text.lower()
    print("\n Skill Analysis Report:")
    print("-" * 40)
    missing_skills = []
    for skill in important_skills:
        count = text_lower.count(skill.lower())
        if count > 0:
            print(f"{skill}:  Found ({count} time(s))")
        else:
            print(f"{skill}:  Not found")
            missing_skills.append(skill)
    
    if missing_skills:
        print("\n Suggestions:")
        print("Consider adding these skills to your resume if applicable:")
        for skill in missing_skills:
            print(f"- {skill}")
    else:
        print("\n Great! Your resume covers all key skills.")

def main():
    parser = argparse.ArgumentParser(description="Analyze a PDF resume for key skills.")
    parser.add_argument("filepath", help="Path to the PDF resume")
    args = parser.parse_args()

    print(f" Reading resume: {args.filepath}")
    text = extract_text_from_pdf(args.filepath)
    
    if text:
        analyze_resume(text)
    else:
        print("No text could be extracted.")

if __name__ == "__main__":
    main()
