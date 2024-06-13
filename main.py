import logging

import coloredlogs

from book import Book

# Create a logger for the main program and the book class
logger = logging.getLogger(__name__)
book_logger = logging.getLogger("Book")
loggers = [logger, book_logger]

# set the loggers' format to include date & time, execution time, hostname, logger name, log level and message
log_format = "%(asctime)-20s (%(msecs)03d) %(hostname)-12s %(name)-16s %(levelname)-8s %(message)s"
for logger_instance in loggers:
    coloredlogs.install(level='DEBUG', logger=logger_instance, fmt=log_format, milliseconds=True)


# Define a "debug it" function that handles both loggers easily
def debug_it(debug_logger=None, level="INFO", message=None):
    if debug_logger is None:
        raise ValueError("No logger defined")
    level = level.upper()
    if level.upper() == "DEBUG":
        debug_logger.debug("🪳 " + message)
    elif level == "WARNING":
        debug_logger.warning("⚠️ " + message)
    elif level == "CRITICAL":
        debug_logger.critical("🆘 " + message)
    elif level == "ERROR":
        debug_logger.error("🚫 " + message)
    elif level == "START":
        debug_logger.info("🛃 START LOGGING ------------")
    elif level == "END":
        debug_logger.info("🛃 END LOGGING   ------------")
    elif level == "INFO":
        debug_logger.info("💭 " + message)


def demo():
    print("Welcome to the Book Class Demo")
    print()

    debug_it(logger, "START")
    debug_it(logger, "DEBUG", "Creating a new book instance...")

    # Instantiate a book with a title and author
    book_1 = Book("Foundation", "Isaac Asimov")

    # Use the book logger to output debug information
    debug_it(book_logger, "DEBUG", f"Book Details: {book_1}")

    print()
    print("Book Title:", book_1.title)
    print("Book Author:", book_1.author)
    print()

    debug_it(logger, "END")

    # Examples of using the debug_it function and logging
    # debug_it(logger, "INFO")
    # debug_it(logger, "INFO", "Informational log entry")
    # debug_it(logger, "DEBUG", "Debug log entry")
    # debug_it(logger, "WARNING", "Warning log entry")
    # debug_it(logger, "ERROR", "Error log entry")
    # debug_it(logger, "CRITICAL", "Critical log entry")


if __name__ == '__main__':
    demo()
