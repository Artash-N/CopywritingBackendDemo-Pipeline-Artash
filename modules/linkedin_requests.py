import anthropic

def initialize_client(api_key):
    return anthropic.Anthropic(api_key=api_key)

def generate_linkedin_request(client, advertising_paragraph, descriptive_paragraph, domain_info, system_prompt):
    user_message = f"""
Information on the person initiating the request (education, company, role, work):
{advertising_paragraph}

Person being contacted by initiator (their education, company, role, work):
{descriptive_paragraph}

Info on the company the person initiating the request is from scapred from their site:
{domain_info}

Generate initial LinkedIn request in under 280 characters. Plain text no formatting or linebreaks. 
"""
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=100,
            temperature = 1.0,
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


def generate_followup_message(client, advertising_paragraph, descriptive_paragraph, domain_info, system_prompt):
    user_message = f"""
The person has accepted the connection request.

Information on the person initiating the request (education, company, role, work):
{advertising_paragraph}

Person being contacted by initiator (their education, company, role, work):
{descriptive_paragraph}

Info on the company the person initiating the request is from scraped from their site:
{domain_info}

Now write a longer follow-up message with more detail on the company and how they think the person they are now connected with could use it. Use a professional but approachable tone.
"""
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=300,
            temperature=1.0,
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
