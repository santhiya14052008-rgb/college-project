import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiDocumentGenerator:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing in .env file"
            )

        self.client = genai.Client(api_key=api_key)

        # Current stable Gemini Flash model.
        self.models = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash",
    "gemini-3.7-flash",
]

        print(f"Using Gemini model: {self.models[0]}")

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        dates
    ):
        prompt = f"""
You are a professional legal document drafting assistant.

Create a complete professional draft legal document.

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Instructions:
- Write a complete and professional legal document.
- Use clear legal language.
- Add appropriate headings and clauses.
- Include parties, obligations, rights, termination,
  confidentiality, dispute resolution, governing law,
  and other relevant clauses when appropriate.
- Do not simply repeat the input fields.
- Do not invent specific laws or legal citations.
- Return only the document text.
- Clearly state that this is a draft for legal review.
"""

        max_attempts = 4

        for attempt in range(max_attempts):
            try:
                response = self.client.models.generate_content(
                    model=self.models[0],
                    contents=prompt
                )

                text = getattr(response, "text", None)

                if not text:
                    raise RuntimeError(
                        "Gemini returned an empty response."
                    )

                return text

            except Exception as e:
                error_text = str(e).lower()

                # Temporary Gemini overload / availability error
                temporary_error = (
                    "503" in error_text
                    or "unavailable" in error_text
                    or "high demand" in error_text
                    or "overloaded" in error_text
                )

                if temporary_error and attempt < max_attempts - 1:
                    wait_time = 5 * (attempt + 1)

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)
                    continue

                raise RuntimeError(
                    f"Gemini generation failed: {e}"
                ) from e
