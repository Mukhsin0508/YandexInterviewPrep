def count_non_intersecting_segments(n, a_b_pairs):
    # Sort the segments by their second element (b), then by the first element (a)
    a_b_pairs.sort(key=lambda x: (x[1], x[0]))

    # Count of non-intersecting segments
    non_intersecting_count = 0

    # The rightmost endpoint of the last non-intersecting segment
    last_non_intersecting_end = float('-inf')

    # Iterate through the sorted segments
    for a, b in a_b_pairs:
        # If the current segment starts after the end of the last non-intersecting segment
        if a > last_non_intersecting_end:
            non_intersecting_count += 1
            last_non_intersecting_end = b  # Update the end of the last non-intersecting segment

    return non_intersecting_count


# Example test case
n = 5
a_b_pairs = [(1, 4), (2, 5), (3, 1), (4, 5), (5, 6)]
print(count_non_intersecting_segments(n, a_b_pairs))  # Expected output: 1
