import time
import uuid

from fastapi import Request


async def request_middleware(
    request: Request,
    call_next,
):
    request_id = str(uuid.uuid4())

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = str(process_time)

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time:.4f}s"
    )

    return response