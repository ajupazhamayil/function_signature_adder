'''
Input:
 * @param string $instanceId The Spanner instance ID.
 * @param string $databaseId The Spanner database ID.
 * @param string $tableName The name of the table to create, defaults to Singers.
 */
function foo($instanceId, $databaseId, $tableName): void

Output:
 * @param string $instanceId The Spanner instance ID.
 * @param string $databaseId The Spanner database ID.
 * @param string $tableName The name of the table to create, defaults to Singers.
 */
function foo(string $instanceId, string $databaseId, string $tableName = 'Singers'): void
'''

import sys
import os
import fileinput


# function_signature string, eg: 'function foo($instanceId, $databaseId)'
# args_in_comment is a list like ['string $instanceId', 'string $databaseId']
#
# Return new function signature
def add_arg_type(function_signature, args_in_comment):
    new_signature = function_signature
    return_type = '): void'
    for arg_comment in args_in_comment:
        arg_name = arg_comment.split(' ')[1]
        # Skip if already the function arguments are in the form 'string $instanceId'
        # Also, skip if the comment is not in sync with function arguments.
        if arg_comment in function_signature or arg_name not in function_signature:
            continue
        else:
            # Replace function 'argument' with 'type argument'
            new_signature = new_signature.replace(arg_name, arg_comment)

    if return_type not in new_signature:
        new_signature = new_signature.replace(')', return_type)

    return new_signature


def get_file_paths(path):
    php_files = []
    # Get all the file names ends with php
    for file in os.listdir(path):
        if file.endswith('.php'):
            php_files.append(os.path.join(path, file))
    return php_files


def process_file(path):
    function_start = 'function '
    param_start = '@param '
    use_keyword = 'use '
    new_args = []
    same = False

    for line in fileinput.input(file, inplace=1):
        if param_start in line:
            # example for param in comment:
            # * @param string $bucketName The name of your Cloud Storage bucket.
            param = line.split(param_start)[1].split(' ')[0:2]
            new_args.append(' '.join(param))
        if function_start in line and use_keyword not in line:
            old_signature = line
            new_signature = add_arg_type(old_signature, new_args)
            if old_signature == new_signature:
                same = True
            line = line.replace(old_signature, new_signature)
            # Reset new_ars for the next functions if peresent
            new_args = []
        sys.stdout.write(line)
    if same:
        print("old_signature equal to new_signature for file ", file, end="\n")


# Run like python filename.py path_to_php_file_directory
if __name__ == "__main__":
    # print(add_arg_type('function foo($instanceId, $databaseId=\'file\')', \
    #    ['string $instanceId', 'string $databaseId']))
    file_paths = get_file_paths(sys.argv[1])
    print("Started processing the following files: \n", file_paths)
    print("Number of files is : \n", len(file_paths))
    for file in file_paths:
        process_file(file)
        print("Completed processing ", file, end="\n")
