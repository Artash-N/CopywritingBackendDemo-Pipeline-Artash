import anthropic

def initialize_client(api_key):
    return anthropic.Anthropic(api_key=api_key)

def generate_linkedin_request(client, advertising_paragraph, descriptive_paragraph, domain_info, system_prompt):
    user_message = f"""
Person initiating the request:
{advertising_paragraph}

Person being contacted:
{descriptive_paragraph}

Info on the company the person initiating the request is from:
{domain_info}

Generate LinkedIn request in under 280 characters. Plain text no formatting or linebreaks. 
"""
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            temperature=1,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        return response.content[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
