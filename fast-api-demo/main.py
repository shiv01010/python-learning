from fastapi import (
    FastAPI,
    Query,
    Cookie,
    Response,
    Header,
    status,
    Form,
    File,
    UploadFile,
    Depends,
)
from products import products
from enum import Enum
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime
from typing import Annotated, Any
from uuid import UUID
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class ModelName(str, Enum):
    tapanai_v0 = "tapanai_v0"
    tapanai_v1 = "tapanai_v1"
    tapanai_v2 = "tapanai_v2"


class SingleCookie(BaseModel):
    key: str
    value: Any
    expires: int
    httponly: bool


# class CookiesToSet(BaseModel):
#     cookies: list[SingleCookie]


class CookiesList(BaseModel):
    tapanai_token: str | None = None
    openai_token: str | None = None
    user_id: str | None = None
    email: str | None = None


class Image(BaseModel):
    image_url: HttpUrl
    image_name: str


class Product(BaseModel):
    id: UUID
    name: str
    price: float
    description: str | None = None
    is_active: bool
    created_at: datetime
    product_images: list[Image]


class User(BaseModel):
    id: str
    first_name: str = Field(description="First name of a user", max_length=12)
    last_name: str = Field(description="last name of user", max_length=15)
    email: EmailStr
    is_active: bool
    user_images: list[Image] | None = None


class UserIn(User):
    password: str


class UserInDB(BaseModel):
    id: str
    first_name: str = Field(description="First name of a user", max_length=12)
    last_name: str = Field(description="last name of user", max_length=15)
    hashed_password: str
    email: EmailStr
    is_active: bool
    user_images: list[Image] | None = None


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/")
def read_root():
    return {"message": "Hello from fastapi"}


@app.post("/products")
def create_one_product(product: Product):
    if any(prod.get("id") == product.id for prod in products):
        return {"message": "Product already exists"}
    else:
        products.append(product.__dict__)
        return products.copy()


@app.get("/products/{product_id}")
def get_one_product(
    product_id: int,
    q: Annotated[str | None, Query(min_length=3, max_length=9, pattern="^king")] = None,
):
    if q:
        return {"q": q, "product_id": product_id}
    for product in products:
        if product["id"] == product_id:
            return product


@app.get("/products")
def get_all_products():
    return products


@app.get("/models/{model_name}")
def get_model_name(model_name: ModelName):
    if model_name is ModelName.tapanai_v0:
        return {"model_name": model_name, "message": "legacy tapanai model"}
    if model_name is ModelName.tapanai_v1:
        return {"model_name": model_name, "message": "updated tapanai model to v1"}
    if model_name is ModelName.tapanai_v2:
        return {"model_name": model_name, "message": "latest king tapan model"}


@app.get("/products/")
def get_items(skip: int = 0, limit: int = 2):
    return products[skip : skip + limit]


@app.post("/multibody")
def post_multi_body(user: User, product: Product):
    return {"user": user, "product": product}


@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(
        key="tapanai_token",
        value="tapan_ai_fhjfhcichfjydtydt",
        expires=36000,
        httponly=True,
    )

    return {"message": "cookie set successfully"}


@app.get("/set-cookies")
def set_cookies(response: Response):
    cookies = [
        {
            "key": "tapanai_token",
            "value": "tapan_ai_fhjfhcichfjydtydt",
            "expires": 36000,
            "httponly": True,
        },
        {
            "key": "openai_token",
            "value": "openai_token_fhjfhcichfjydtydt",
            "expires": 36000,
            "httponly": True,
        },
        {
            "key": "user_id",
            "value": "user_king_tapan",
            "expires": 36000,
            "httponly": True,
        },
        {
            "key": "email",
            "value": f"tapan@tapatap.ai",
            "expires": 36000,
            "httponly": True,
        },
    ]

    for cookie in cookies:
        response.set_cookie(
            key=cookie.get("key"),
            value=cookie.get("value"),
            expires=cookie.get("expires"),
            httponly=cookie.get("httponly"),
        )

    return {"message": "many cookes set successfully"}


@app.get("/get-cookie")
def get_cookies(
    tapanai_token: Annotated[str | None, Cookie()],
):
    return {"tapanai_token": tapanai_token}


@app.get("/get-cookies")
def get_cookies(
    cookies: Annotated[CookiesList, Cookie()],
):
    return cookies


@app.get("/items/")
async def read_items(
    headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
):
    return headers


@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserIn) -> User:
    user_saved = fake_save_user(user_in)
    return user_saved


@app.delete("/user/{id}")
async def delete_user(id: str):
    return {"id": id}


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really", user_in_db)
    return user_in_db


@app.post("/login", status_code=200)
def login(
    resume: Annotated[bytes, File()],
):
    return {"resume": len(resume)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@app.get("/authdemo/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


