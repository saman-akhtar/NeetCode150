ith test cases


# Set
# Get
# Delete are methods in Key value store


# for transactions
# Begin
# Commit
# Rollback
class KeyValueStore:
    def __init__(self):
        self.permanent_store = {}  # Permanent key-value storage
        self.transaction_stack = []  # Stack to handle nested transactions

    def set(self, key, value):
        if self.transaction_stack:
            self.transaction_stack[-1][key] = value
        else:
            self.permanent_store[key] = value

    def get(self, key):
        # Look for the key in the current transaction stack
        for transaction in reversed(self.transaction_stack):
            if key in transaction:
                return transaction[key]
        # If not found in transactions, look in the permanent store
        return self.permanent_store.get(key, None)

    def delete(self, key):
        self.set(key, None)  # Mark the key as deleted with a None value

    def begin(self):
        self.transaction_stack.append({})  # Start a new transaction

    def commit(self):
        if not self.transaction_stack:
            raise Exception("No transaction to commit")

        # Merge the current transaction into the previous one or the permanent store
        current_transaction = self.transaction_stack.pop()
        if self.transaction_stack:
            # Merge into the previous transaction
            self.transaction_stack[-1].update(current_transaction)
        else:
            # Apply changes to the permanent store
            for key, value in current_transaction.items():
                if value is None:
                    self.permanent_store.pop(key, None)  # Delete if marked for deletion
                else:
                    self.permanent_store[key] = value

    def rollback(self):
        if not self.transaction_stack:
            raise Exception("No transaction to rollback")
        self.transaction_stack.pop()  # Discard the current transaction

# Test cases to validate functionality
if __name__ == "__main__":
    kv_store = KeyValueStore()

    # Basic operations
    kv_store.set("a", 10)
    assert kv_store.get("a") == 10

    kv_store.delete("a")
    assert kv_store.get("a") is None

    # Transactions
    kv_store.begin()
    kv_store.set("a", 20)
    assert kv_store.get("a") == 20

    kv_store.rollback()
    assert kv_store.get("a") is None

    kv_store.begin()
    kv_store.set("a", 30)
    kv_store.commit()
    assert kv_store.get("a") == 30

    # Nested transactions
    kv_store.begin()
    kv_store.set("b", 40)
    kv_store.begin()
    kv_store.set("b", 50)
    assert kv_store.get("b") == 50
    kv_store.rollback()
    assert kv_store.get("b") == 40
    kv_store.commit()
    assert kv_store.get("b") == 40

    print("All test cases passed!")
