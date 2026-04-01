import subprocess

def analyze_reviews(reviews):
    text = "\n".join(reviews)
    prompt = f"""
You are a marketing analyst.

Please analyze the following customer reviews carefully.

Requirements:
1. Identify the most frequently mentioned problems or complaints by customers.
2. Determine whether each review is positive or negative.
3. Extract the most common words, themes, or issues mentioned in the complaints.
4. Provide a clear and concise summary of the main customer issues.
5. Give practical recommendations for the company to improve the product or service.

Reviews:
{text}
"""
    process = subprocess.Popen(
        ["ollama", "run", "phi3:mini"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, error = process.communicate(input=prompt)

    if error:
        print("Error from Ollama:", error)
    return output