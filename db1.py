

        except httpx.HTTPError as e:
            await self.error_repo.insert_error(
                Error(
                    tool_name="code_base_search",
                    error_message=f"Error in upsert vectors http error : {str(e)}",
                )
            )
            raise H
                    tool_name="code_base_search",
