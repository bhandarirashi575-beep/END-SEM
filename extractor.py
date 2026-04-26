def extract_data(raw_text):
    if "Error" in raw_text:
        return "Fallback: Unable to process data due to API issue."

    from utils.llm import call_llm

    prompt = f"""
    Extract key environmental impacts:

    {raw_text[:2000]}
    """

    return call_llm(prompt)