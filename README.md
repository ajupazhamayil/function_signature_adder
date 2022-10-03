# PHP Function Signature Changer

This repository helps to change the old PHP function signatures (version < 7.4.0) to new PHP function signatures with type declarations(version >= 7.4.0).

More information on the type declaration is available here https://www.php.net/manual/en/language.types.declarations.php

# How to use this script

Run `python signature_argument_adder.py path_to_directory`
where `path_to_directory` is the path to the php files' directory

**Note: This script will NOT disturb the existing new PHP function signatures in the directory**

# Requirements
The `python3` script expects proper `@param` comments for all the variables in the function signature.

eg:
```
 /*
 * @param string $instanceId The Spanner instance ID.
 * @param string $databaseId The Spanner database ID.
 * @param string $tableName The name of the table to create, defaults to Singers.
 */
function foo($instanceId, $databaseId, $tableName)
```

# Input and Output example

```
Input:
 /*
 * @param string $instanceId The Spanner instance ID.
 * @param string $databaseId The Spanner database ID.
 * @param string $tableName The name of the table to create, defaults to Singers.
 */
function foo($instanceId, $databaseId, $tableName)

Output:
 /*
 * @param string $instanceId The Spanner instance ID.
 * @param string $databaseId The Spanner database ID.
 * @param string $tableName The name of the table to create, defaults to Singers.
 */
function foo(string $instanceId, string $databaseId, string $tableName = 'Singers'): void
```


**Feel free to raise any issues/suggestions in the repository**
