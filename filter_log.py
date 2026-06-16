# Import defaultdict from collections module.
# defaultdict automatically creates an empty list for a new key.
from collections import defaultdict

# Sample log data
logs = [
    "2026-06-16 10:00:01 INFO    Application started successfully",
    "2026-06-16 10:00:05 INFO    Connected to database",
    "2026-06-16 10:05:12 WARNING Database response time is high (3.5 sec)",
    "2026-06-16 10:05:15 WARNING Disk usage reached 85%",
    "2026-06-16 10:10:20 ERROR   Failed to connect to payment service",
    "2026-06-16 10:10:21 ERROR   Connection timeout after 30 seconds",
    "2026-06-16 10:15:00 INFO    Retry successful, payment service connected"
]

# Create a dictionary where each new key gets an empty list by default.
# Example:
# {
#   "INFO": [],
#   "WARNING": [],
#   "ERROR": []
# }
result = defaultdict(list)

# Loop through each log entry
for log in logs:

    # Split the string into 4 parts only:
    # Part 0 -> Date
    # Part 1 -> Time
    # Part 2 -> Log Level (INFO/WARNING/ERROR)
    # Part 3 -> Remaining message
    #
    # Example:
    # "2026-06-16 10:10:20 ERROR Failed to connect to payment service"
    #
    # becomes:
    # [
    #   '2026-06-16',
    #   '10:10:20',
    #   'ERROR',
    #   'Failed to connect to payment service'
    # ]
    parts = log.split(maxsplit=3)

    # Extract the log level
    level = parts[2]

    # Extract the actual log message
    message = parts[3]

    # Append the message to the corresponding log level list
    #
    # Example:
    # result["ERROR"].append("Failed to connect to payment service")
    result[level].append(message)

# Convert defaultdict to normal dictionary and print the result
print(dict(result))
