def leaky_bucket():
    print("LEAKY BUCKET ALGORITHM")
    capacity = int(input("Enter the bucket size: "))
    rate = int(input("Enter the processing rate: "))
    seconds = int(input("Enter the number of seconds to simulate: "))

    if capacity <= 0 or rate <= 0 or seconds < 0:
        print("Bucket size and processing rate must be positive; seconds cannot be negative.")
        return

    packets = []
    for i in range(seconds):
        value = int(input(f"Enter the size of the packet entering at {i + 1} sec: "))
        if value < 0:
            print("Packet size cannot be negative.")
            return
        packets.append(value)

    count = 0
    print("\nSecond | Packet Received | Packet Sent | Packet Left | Dropped")
    print("---------------------------------------------------------------")

    for i in range(seconds):
        dropped = 0
        count += packets[i]
        if count > capacity:
            dropped = count - capacity
            count = capacity

        sent = min(count, rate)
        count -= sent
        print(f"{i + 1:>6} | {packets[i]:>15} | {sent:>11} | {count:>11} | {dropped:>7}")

    # Empty the remaining bucket after the input period.
    second = seconds
    while count > 0:
        second += 1
        sent = min(count, rate)
        count -= sent
        print(f"{second:>6} | {0:>15} | {sent:>11} | {count:>11} | {0:>7}")


if __name__ == "__main__":
    leaky_bucket()
