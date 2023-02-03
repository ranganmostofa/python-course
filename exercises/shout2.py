# file_name = input("Enter file name: ")
#
# line_count = 0
# total = 0
# with open(file_name, "r") as file_obj:
#     while line := file_obj.readline():
#         if "X-DSPAM-Confidence:" in line:
#             total += float(line[20:])
#             line_count += 1
#
#     print(f"Average spam confidence: {total / line_count}")

file_name = input("Enter file name: ")
if file_name == "knock knock":
    print("who's there?")
else:
    line_count = 0
    total = 0
    with open(file_name, "r") as file_obj:
        for line in file_obj.readlines():
            if "X-DSPAM-Confidence:" in line:
                total += float(line[20:])
                line_count += 1

        print(f"Average spam confidence: {total / line_count}")
