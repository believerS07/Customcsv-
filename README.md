# Customcsv
csv = CustomCSV("students.csv")
headers = csv.get_headers()
rows = csv.get_rows()

# Delete a line
csv.delete_row(2)

# Replace a line
csv.replace_row(1, ["2", "Robert", "robert@example.com"])

# Create a copy
csv.copy_file("students_backup.csv")

# Clear the file
csv.clear_file()
