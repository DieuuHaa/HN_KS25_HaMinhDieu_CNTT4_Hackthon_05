from fastapi import HTTPException, status
def book_not_found():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Không tìm thấy sách"
    )

