# Online Python compiler (interpreter) to run Python online.
class Cell:
    def __init__(self):
        self.value = 0  # The value of the cell
        self.references = {}  # Tracks other cells contributing to this cell's value

class Excel:
    def __init__(self, H: int, W: str):
        self.width = ord(W) - ord('A') + 1  # Convert column letter to a number
        self.sheet = [[Cell() for _ in range(self.width)] for _ in range(H)]  # Create an H x W grid of cells

    def set(self, r: int, c: str, v: int) -> None:
        """Set the value of a cell and remove any formula."""
        cell = self.sheet[r - 1][ord(c) - ord('A')]
        cell.value = v  # Directly set the value
        cell.references = {}  # Clear references (no formula now)

    def sum(self, r: int, c: str, strs: list[str]) -> int:
        """Set the cell as a formula summing specified cells."""
        cell = self.sheet[r - 1][ord(c) - ord('A')]
        cell.references = {}  # Clear previous references
        cell.is_formula = True  # Mark as formula
        total = 0
    
        for st in strs:
            if ':' not in st:
                # Single cell
                row, col = int(st[1:]), st[0]
                cell.references[(row, col)] = 1
                total += self.get(row, col)
            else:
                # Range of cells
                start, end = st.split(':')
                start_row, start_col = int(start[1:]), start[0]
                end_row, end_col = int(end[1:]), end[0]
                for row in range(start_row, end_row + 1):
                    for col_index in range(ord(start_col), ord(end_col) + 1):
                        col = chr(col_index)
                        cell.references[(row, col)] = 1
                        total += self.get(row, col)
    
        cell.value = total  # Store the calculated total
        return total

    def get(self, r: int, c: str) -> int:
        """Get the value of a cell."""
        cell = self.sheet[r - 1][ord(c) - ord('A')]
        if cell.references:
            return self._calculate_sum(r, c)  # Recalculate for formulas
        return cell.value





    
                        


    def _calculate_sum(self, r: int, c: str) -> int:
        """Calculate the sum of the referenced cells."""
        cell = self.sheet[r - 1][ord(c) - ord('A')]
        total = 0
        for (row, col), _ in cell.references.items():
            total += self.get(row, col)  # Recursively calculate
        cell.value = total  # Update the cell's value
        return total
def test_excel_operations():
    # Step 1: Initialize Excel with 3 rows and columns up to "C"
    ex = Excel(3, 'C')

    # Test 1: Get value of an uninitialized cell
    assert ex.get(1, "A") == 0, "Test 1 Failed: Uninitialized cell should return 0"

    # Step 2: Set value for cell "A1"
    ex.set(1, "A", 2)

    # Test 2: Check if the value of "A1" is updated
    assert ex.get(1, "A") == 2, "Test 2 Failed: 'A1' should be 2 after setting it"

    # Step 3: Set value for cell "B1"
    ex.set(1, "B", 3)

    # Test 3: Check if the value of "B1" is updated
    assert ex.get(1, "B") == 3, "Test 3 Failed: 'B1' should be 3 after setting it"

    # Step 4: Set up a sum in cell "C2" with an empty range
    result = ex.sum(2, "C", [])

    # Test 4: Check the sum when the range is empty
    assert result == 0, "Test 4 Failed: 'C2' should sum to 0 when the range is empty"
    assert ex.get(2, "C") == 0, "Test 4 Failed: 'C2' should store the value 0"

    print("All tests passed!")


# Run the test case
# test_excel_operations()
def test_excel_sum():
    # Step 1: Initialize Excel with 3 rows and columns up to "C"
    ex = Excel(3, 'C')

    # Step 2: Set values for specific cells
    ex.set(1, "A", 2)   # A1 = 2
    ex.set(1, "B", 3)   # B1 = 3
    ex.set(2, "A", 4)   # A2 = 4
    ex.set(2, "B", 5)   # B2 = 5

    # Step 3: Perform sum operation
    result = ex.sum(3, "C", ["A1", "A1:B2"])  # C3 = A1 + (A1:B2)

    # Print intermediate and final results
    print("Sum of A1 + (A1:B2):", result)       # Should print the calculated sum
    print("Value in C3:", ex.get(3, "C"))       # Should match the calculated sum

    # Assertions to ensure correctness
    expected_sum = 2 + (2 + 3 + 4 + 5)  # A1 + A1:B2 = 2 + (2+3+4+5) = 16
    assert result == expected_sum, f"Test Failed: Expected sum {expected_sum}, got {result}"
    assert ex.get(3, "C") == expected_sum, f"Test Failed: C3 should be {expected_sum}"

    print("Test passed successfully!")

# Run the test function
test_excel_sum()
