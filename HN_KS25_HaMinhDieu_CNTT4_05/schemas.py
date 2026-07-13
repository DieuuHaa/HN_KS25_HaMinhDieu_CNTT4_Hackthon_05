from pydantic import BaseModel, Field

class CreateBook(BaseModel):
    title: str = Field(
        ...,
        min_length = 3,
        max_length = 100,
        decription = "Tên sách"
    )

    author: str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        decription = "Tên tác giả"
    )

    category: str = Field(
        ...,
        min_length = 3,
        max_length = 20,
        decription = "Thể loại"
    )

    quantity: int = Field(
        ...,
        ge = 1,
        decription = "Số lượng sách còn lại"
    )

class UpdateBook(BaseModel):
    title: str = Field(
        ...,
        min_length = 3,
        max_length = 100,
        decription = "Tên sách"
    )

    author: str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        decription = "Tên tác giả"
    )

    category: str = Field(
        ...,
        min_length = 3,
        max_length = 20,
        decription = "Thể loại"
    )

    quantity: int = Field(
        ...,
        ge = 1,
        decription = "Số lượng sách còn lại"
    )