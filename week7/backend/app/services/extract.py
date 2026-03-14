import re


def extract_action_items(text: str) -> list[str]:
    # Split on sentence-ending punctuation or line boundaries
    raw_sentences = re.split(r'(?<=[.!?])\s+|\n+', text)

    action_pattern = re.compile(
        r'\b(need to|must|should|will|have to|has to|please|make sure|ensure)\b',
        re.IGNORECASE,
    )

    results: list[str] = []
    for sentence in raw_sentences:
        # Strip leading bullet points, dashes, or numbered list markers (e.g. "- ", "1. ", "* ")
        cleaned = re.sub(r'^[\s]*(?:[-*•]|\d+[.):\-])\s*', '', sentence).strip()

        if not cleaned:
            continue

        # Exclude questions
        if cleaned.endswith('?'):
            continue

        # Include only sentences containing action verbs
        if action_pattern.search(cleaned):
            results.append(cleaned)

    return results


