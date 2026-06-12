from llm.gemini_service import GeminiService

service = GeminiService()

response = service.generate_content(
    "Say hello in one sentence."
)

print(response)