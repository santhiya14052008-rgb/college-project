import logging

from fastapi import APIRouter, HTTPException

from .schemas import DocumentRequest, DocumentResponse
from .gemini_generator import GeminiDocumentGenerator


logger = logging.getLogger(__name__)

router = APIRouter()

generator = GeminiDocumentGenerator()


@router.post(
    "/generate",
    response_model=DocumentResponse,
    tags=["Documents"]
)
def generate_document(request: DocumentRequest):

    try:

        generated_text = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates,
        )

        return DocumentResponse(
            success=True,
            document_type=request.document_type,
            content=generated_text,
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    except Exception as error:

        logger.exception(
            "Document generation failed"
        )

        raise HTTPException(
            status_code=502,
            detail=f"AI generation failed: {error}"
        ) from error
