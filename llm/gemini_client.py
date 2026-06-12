from llm.gemini_service import GeminiService

service = GeminiService()

response = service.generate_content(
    "Explain Cyber Security in 5 lines."
)

print(response)