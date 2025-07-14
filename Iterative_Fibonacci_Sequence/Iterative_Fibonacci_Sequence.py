def fibonacci_iterative(n_terms):
    """
    Displays the Fibonacci sequence up to a specified number of term using an iterative approach.

    Args:
        n_terms (int): The number of terms to display in the sequence. n_terms must be a non-negative integer.
    """
    if n_terms <= 0:
        print("Please enter a positive integer for the number of terms.")
    elif n_terms == 1:
        print("Fibonacci sequence up to 1 term:")
        print(0)
    else:
        a, b = 0, 1
        print(f"Fibonacci sequence up to {n_terms} terms:")
        print(a)  # Print the first term
        print(b)  # Print the second term

        for _ in range(2, n_terms):  # Start from the 3rd term
            next_term = a + b
            print(next_term)
            a = b
            b = next_term

# --- Examples ---

print("--- Iterative Fibonacci ---")
fibonacci_iterative(10) # Display 10 terms
print("\n--- Another Example ---")
fibonacci_iterative(1)  # Display 1 term
print("\n--- Edge Case ---")
fibonacci_iterative(5)  # Handle invalid input
