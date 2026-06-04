log_file = "sample_log.txt"

info_count = 0
warning_count = 0
error_count = 0

error_lines = []
warning_lines = []

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
            warning_lines.append(line)
        elif "ERROR" in line:
            error_count += 1
            error_lines.append(line)

print("Log analysis completed.")
print("INFO count:", info_count)
print("WARNING count:", warning_count)
print("ERROR count:", error_count)

print("\nWarning details:")
for warning in warning_lines:
    print("-", warning)

print("\nError details:")
for error in error_lines:
    print("-", error)
