"""Configure server for the MessageServicer."""

import logging
from concurrent import futures

import grpc

from . import MessageServicer, add_MessageServicer_to_server, message_pb2

LOGGER = logging.getLogger(__name__)


def initialise_logger() -> None:
    """Configure and initialize the application logger.

    Set up console and file handlers with appropriate log levels
    and formatting.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    if not root_logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        root_logger.addHandler(stream_handler)


def log_request(func):
    """Log the request.

    Args:
        func: The request handler function to wrap.
    """

    def wrapper(self, request, context):
        """Wrapper for SendMessage."""
        LOGGER.info(
            "Received SendMessage | count=%s | message=%s",
            request.count,
            request.message,
        )
        return func(self, request, context)

    return wrapper


def repeat_message_count_times(count, message):
    """Yield message for count times.

    Args:
        count: Number of times the message to be yielded.
        message: Message to be yield.

    Yields:
        Message with the s.no.
    """
    for i in range(count):
        yield message_pb2.MessageResponse(reply=f"{i+1}. {message}")


class Message(MessageServicer):
    """A message service that sends the message, number of times the client requested.

    Args:
        MessageServicer: gRPC service class generated from the .proto file.
    """

    @log_request
    def SendMessage(  # type: ignore[return] # noqa: N802 function name should be lowercase
        self, request, context
    ):
        """Send message and process it.

        Args:
            request: MessageRequest containing the Message and the count.
            context: gRPC context object for the request.

        Yields:
            MessageResponse as a stream.
        """
        for response in repeat_message_count_times(request.count, request.message):
            yield response


def start_server():
    """Start the gRPC server and register the service with the service registry."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MessageServicer_to_server(
        Message(),
        server,
    )
    listen_address = "localhost:50051"
    server.add_insecure_port(listen_address)
    print(f"Server started and listening on : {listen_address}.")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    initialise_logger()
    start_server()
