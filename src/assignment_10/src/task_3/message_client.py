"""Client that demonstrates the server communication."""

import grpc
from src.task_3.stubs.message_pb2 import MessageRequest  # type: ignore
from src.task_3.stubs.message_pb2_grpc import MessageStub  # type: ignore


def repeat_message_grpc(count: int, message: str) -> None:
    """Create channel and send the message to the server."""
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = MessageStub(channel)
        responses = stub.SendMessage(MessageRequest(message=message, count=count))

        for response in responses:
            print(response.reply)


if __name__ == "__main__":
    repeat_message_grpc(5, "Hello")
