from utils.llm import call_llm

def write_brief(structured_data, topic):
    prompt = f"""
    Write a professional environmental impact brief on: {topic}

    Include:
    - Introduction
    - Key Findings
    - Risks
    - Conclusion

    DATA:
    {structured_data}
    """

    return call_llm(prompt)