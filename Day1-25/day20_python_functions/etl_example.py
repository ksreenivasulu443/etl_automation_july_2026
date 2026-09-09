def count_check(source_count,target_count):
    print("source_count is", source_count)
    print("targte_count is", target_count)
    status=None
    if source_count == target_count:
        status = "PASS"

    elif source_count > target_count:
        status = "FAIL"

    return status



print(count_check(source_count=10, target_count=12))
#
# print(count_check(source_count=10, target_count=10))
#
# status = count_check(source_count=11, target_count=10)

# print(status)