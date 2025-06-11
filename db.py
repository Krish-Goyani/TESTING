import asyncio
import time
from datetime import datetime
from typing import Any, Dict
import asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repoimport asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repo
import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone

import asyncio
import time
from datetime import datetime
from typing import Any, Dict
import asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repoimport asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repo
import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repo: ErrorRepo = Depends(ErrorRepo)):
        self.pinecone_api_key = settings.PINECONE_API_KEY
        self.api_version = settings.PINECONE_API_VERSION
        self.index_url = settings.PINECONE_CREATE_INDEX_URL
        self.dense_embed_url = settings.PINECONE_EMBED_URL
        self.upsert_url = settings.PINECONE_UPSERT_URL
        self.query_url = settings.PINECONE_QUERY_URL
        self.list_index_url = settings.PINECONE_LIST_INDEXES_URL
        self.semaphore = asyncio.Semaphore(10)
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.error_repo = error_repo
        self.timeout = httpx.Timeout(
            connect=60.0,  # Time to establish a connection
            read=120.0,  # Time to read the response
            write=120.0,  # Time to send data
            pool=60.0,  # Time to wait for a connection from the pool
        )

    async def list_pinecone_indexes(self):
        url = self.list_index_url

        headers = {
            "Api-Key": self.pinecone_api_key,
            "X-Pinecone-API-Version": self.api_version,
        }

        try:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in listing pinecone indexes HTTPStatusError : {e.response.text} - {str(e)}",
                )
            )
            raise HTTPException(
                status_code=400,
                detail=f"Error in listing pinecone indexes HTTPStatusError: {e.response.text} - {str(e)}",
            )
        except Exception as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in pinecone list indexes: {str(e)}",
                )
            )
            raise HTTPException(
                status_code=500,
                detail=f"Error in pinecone list indexes: {str(e)}",
            )

    async def create_index(
        self, index_name: str, dimension: int, metric: str
    ) -> Dict[str, Any]:
        print(
            f"Creating index {index_name} with dimension {dimension} and metric {metric}"
        )
        if self.pc.has_index(index_name) == False:
            index_data = {
                "name": index_name,
                "dimension": dimension,
                "metric": metric,
                "spec": {"serverless": {"cloud": "aws", "region": "us-east-1"}},
            }

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": self.pinecone_api_key,
                "X-Pinecone-API-Version": self.api_version,
            }

            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.post(
                        self.index_url, headers=headers, json=index_data
                    )
                    response.raise_for_status()

                    retry_count = 0
                    max_retries = 30
                    while retry_count < max_retries:
                        status = (
                            self.pc.describe_index(index_name)
                            .get("status")
                            .get("state")
                        )
                        loggers["main"].info(f"Index status: {status}")

                        if status == "Ready":
                            loggers["main"].info(f"Index {index_name} is ready")
                            break

                        retry_count += 1
                        time.sleep(2)

                    if retry_count > max_retries:
                        raise HTTPException(
                            status_code=500, detail="Index creation timed out"
                        )

                    loggers["main"].info("Index Created")
                    return response.json()

            except httpx.HTTPStatusError as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                    )
                )

                raise HTTPException(
                    status_code=400,
                    detail=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                )
            except Exception as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index: {str(e)}",
                    )
                )
                raise HTTPException(
                    status_code=500, detail=f"Error creating index: {str(e)}"
                )
def get_pinecone_service(
    error_repo: ErrorRepo = Depends(ErrorRepo)
) -> PineconeService:
    return PineconeService(error_repo=error_repo)import asyncio
import time
from datetime import datetime
from typing import Any, Dict
import asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repoimport asyncio
import time
from datetime import datetime
from typing import Any, Dict

import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repo
import httpx
from fastapi import Depends, HTTPException
from pinecone import Pinecone



class PineconeService:
    def __init__(self, error_repo: ErrorRepo = Depends(ErrorRepo)):
        self.pinecone_api_key = settings.PINECONE_API_KEY
        ings.PINECONE_LIST_INDEXES_URL
        self.semaphore = asyncio.Semaphore(10)
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.error_repo = error_repo
        self.timeout = httpx.Timeout(
            connect=60.0,  # Time to establish a connection
            read=120.0,  # Time to read the response
            write=120.0,  # Time to send data
            pool=60.0,  # Time to wait for a connection from the pool
        )

    async def list_pinecone_indexes(self):
        url = self.list_index_url

        headers = {
            "Api-Key": self.pinecone_api_key,
            "X-Pinecone-API-Version": self.api_version,
        }

        try:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in listing pinecone indexes HTTPStatusError : {e.response.text} - {str(e)}",
                )
            )
            raise HTTPException(
                status_code=400,
                detail=f"Error in listing pinecone indexes HTTPStatusError: {e.response.text} - {str(e)}",
            )
        except Exception as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in pinecone list indexes: {str(e)}",
                )
            )
            raise HTTPException(
                status_code=500,
                detail=f"Error in pinecone list indexes: {str(e)}",
            )

    async def create_index(
        self, index_name: str, dimension: int, metric: str
    ) -> Dict[str, Any]:
        print(
            f"Creating index {index_name} with dimension {dimension} and metric {metric}"
        )
        if self.pc.has_index(index_name) == False:
            index_data = {
                "name": index_name,
                "dimension": dimension,
                "metric": metric,
                "spec": {"serverless": {"cloud": "aws", "region": "us-east-1"}},
            }

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": self.pinecone_api_key,
                "X-Pinecone-API-Version": self.api_version,
            }

            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.post(
                        self.index_url, headers=headers, json=index_data
                    )
                    response.raise_for_status()

                    retry_count = 0
                    max_retries = 30
                    while retry_count < max_retries:
                        status = (
                            self.pc.describe_index(index_name)
                            .get("status")
                            .get("state")
                        )
                        loggers["main"].info(f"Index status: {status}")

                        if status == "Ready":
                            loggers["main"].info(f"Index {index_name} is ready")
                            break

                        retry_count += 1
                        time.sleep(2)

                    if retry_count > max_retries:
                        raise HTTPException(
                            status_code=500, detail="Index creation timed out"
                        )

                    loggers["main"].info("Index Created")
                    return response.json()

            except httpx.HTTPStatusError as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                    )
                )

                raise HTTPException(
                    status_code=400,
                    detail=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                )
            except Exception as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index: {str(e)}",
                    )
                )
                raise HTTPException(
                    status_code=500, detail=f"Error creating index: {str(e)}"
                )
def get_pinecone_service(
    error_repo: ErrorRepo = Depends(ErrorRepo)
) -> PineconeService:
repo: ErrorRepo = Depends(ErrorRepo)):
        self.pinecone_api_key = settings.PINECONE_API_KEY
        self.api_version = settings.PINECONE_API_VERSION
        self.index_url = settings.PINECONE_CREATE_INDEX_URL
        self.dense_embed_url = settings.PINECONE_EMBED_URL
        self.upsert_url = settings.PINECONE_UPSERT_URL
        self.query_url = settings.PINECONE_QUERY_URL
        self.list_index_url = settings.PINECONE_LIST_INDEXES_URL
        self.semaphore = asyncio.Semaphore(10)
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.error_repo = error_repo
        self.timeout = httpx.Timeout(
            connect=60.0,  # Time to establish a connection
            read=120.0,  # Time to read the response
            write=120.0,  # Time to send data
            pool=60.0,  # Time to wait for a connection from the pool
        )

    async def list_pinecone_indexes(self):
        url = self.list_index_url

        headers = {
            "Api-Key": self.pinecone_api_key,
            "X-Pinecone-API-Version": self.api_version,
        }

        try:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in listing pinecone indexes HTTPStatusError : {e.response.text} - {str(e)}",
                )
            )
            raise HTTPException(
                status_code=400,
                detail=f"Error in listing pinecone indexes HTTPStatusError: {e.response.text} - {str(e)}",
            )
        except Exception as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in pinecone list indexes: {str(e)}",
                )
            )
            raise HTTPException(
                status_code=500,
                detail=f"Error in pinecone list indexes: {str(e)}",
            )

    async def create_index(
        self, index_name: str, dimension: int, metric: str
    ) -> Dict[str, Any]:
        print(
            f"Creating index {index_name} with dimension {dimension} and metric {metric}"
        )
        if self.pc.has_index(index_name) == False:
            index_data = {
                "name": index_name,
                "dimension": dimension,
                "metric": metric,
                "spec": {"serverless": {"cloud": "aws", "region": "us-east-1"}},
            }

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": self.pinecone_api_key,
                "X-Pinecone-API-Version": self.api_version,
            }

            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.post(
                        self.index_url, headers=headers, json=index_data
                    )
                    response.raise_for_status()

                    retry_count = 0
                    max_retries = 30
                    while retry_count < max_retries:
                        status = (
                            self.pc.describe_index(index_name)
                            .get("status")
                            .get("state")
                        )
                        loggers["main"].info(f"Index status: {status}")

                        if status == "Ready":
                            loggers["main"].info(f"Index {index_name} is ready")
                            break

                        retry_count += 1
                        time.sleep(2)

                    if retry_count > max_retries:
                        raise HTTPException(
                            status_code=500, detail="Index creation timed out"
                        )

                    loggers["main"].info("Index Created")
                    return response.json()

            except httpx.HTTPStatusError as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                    )
                )

                raise HTTPException(
                    status_code=400,
                    detail=f"Error creating index HTTPStatusError: {e.response.text} - {str(e)}",
                )
            except Exception as e:
                await self.error_repo.insert_error(
                    Error(
                        tool_name="code_base_search",
                        error_message=f"Error creating index: {str(e)}",
                    )
                )
                raise HTTPException(
                    status_code=500, detail=f"Error creating index: {str(e)}"
                )
def get_pinecone_service(
    error_repo: ErrorRepo = Depends(ErrorRepo)
) -> PineconeService:
    return PineconeService(error_repo=error_repo)