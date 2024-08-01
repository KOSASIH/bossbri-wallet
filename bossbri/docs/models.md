# Models
=======

## Wallet

### Fields

* `id`: Unique identifier for the wallet.
* `user`: The user associated with the wallet.
* `balance`: The current balance of the wallet.
* `created_at`: Timestamp when the wallet was created.
* `updated_at`: Timestamp when the wallet was last updated.

## Transaction

### Fields

* `id`: Unique identifier for the transaction.
* `wallet`: The wallet associated with the transaction.
* `transaction_type`: The type of transaction (deposit, withdrawal, or transfer).
* `amount`: The amount of the transaction.
* `description`: A description of the transaction.
* `created_at`: Timestamp when the transaction was created.
* `updated_at`: Timestamp when the transaction was last updated.

## Address

### Fields

* `id`: Unique identifier for the address.
* `wallet`: The wallet associated with the address.
* `address`: The actual address.
* `label`: A label for the address.
* `created_at`: Timestamp when the address was created.
* `updated_at`: Timestamp when the address was last updated.
