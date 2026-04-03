from google import genai
import re

# 3. Sub-Agent Logic 
async def run_sub_agent(client, agent_name: str, task: str, company: str):
    """Executes a specialized agent task with token limits"""
    prompt = f"You are the {agent_name}. Research the following for {company}: {task}. Provide 3 short key insights.No intro, no outro.Keep it under 200 words."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "max_output_tokens": 2000, 
                "temperature": 0.2        
            }
        )

        clean_text = re.sub(r'\*', '', response.text).strip()
        return {agent_name: clean_text}
    except Exception as e:
        return {agent_name: f"Agent Error: {str(e)}"}