import re
import json

def clean_structured_output(response_text):
    """Extract structured data from chatty LLM output"""
    
    # Try JSON extraction first
    json_match = re.search(r'\[.*\]|\{.*\}', response_text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            pass
    
    # Extract numbered lists
    numbered_items = re.findall(r'^\d+\.\s*(.+)$', response_text, re.MULTILINE)
    if numbered_items:
        return numbered_items
    
    # Extract bullet points
    bullet_items = re.findall(r'^\s*[-*•]\s*(.+)$', response_text, re.MULTILINE)
    if bullet_items:
        return bullet_items
    
    # Fallback: split on newlines and clean
    lines = [line.strip() for line in response_text.split('\n') if line.strip()]
    return [line for line in lines if not line.lower().startswith(('here', 'the', 'in summary'))]

def clean_for_prompt(text):
    """Clean untrusted text for safe use in prompts"""
    if not text:
        return ""
    
    # Remove/escape problematic characters
    cleaned = text.replace('"', '\\"')  # Escape quotes
    cleaned = cleaned.replace("'", "\\'")  # Escape single quotes
    cleaned = cleaned.replace('\n', ' ')   # Replace newlines with spaces
    cleaned = cleaned.replace('\r', '')    # Remove carriage returns
    cleaned = cleaned.replace('\t', ' ')   # Replace tabs with spaces
    cleaned = cleaned.replace('{', '{{')
    cleaned = cleaned.replace('}','}}') # Escape brackets.
    
    # Limit length (prevents prompt injection and token overflow)
    if len(cleaned) > 1000:  # Adjust based on your needs
        cleaned = cleaned[:997] + "..."
    
    return cleaned.strip()

def build_prompt_safely(template, **kwargs):
    """Build prompts with automatic cleaning"""
    cleaned_kwargs = {}
    for key, value in kwargs.items():
        if isinstance(value, str):
            cleaned_kwargs[key] = clean_for_prompt(value)
        else:
            cleaned_kwargs[key] = value
    
    return template.format(**cleaned_kwargs)

# Usage
# prompt = build_prompt_safely(
#     "Verify this claim: {claim}\n\nEvidence: {evidence}",
#     claim="Climate change affects agriculture",
#     evidence=untrusted_search_results
# )