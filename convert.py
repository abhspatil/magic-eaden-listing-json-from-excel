import json
import openpyxl

def excel_to_json(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        nft = {
            "id": row[0],
            "meta": {
                "name": row[1],
                "high_res_img_url": row[2],
                "attributes": [
                    {
                        "trait_type": row[3],
                        "value": row[4]
                    }
                ]
            }
        }

        data.append(nft)

    return data

file_path = 'Listing.xlsx'
json_data = excel_to_json(file_path)

json_string = json.dumps(json_data, indent=4)
print(json_string)

# If you want to save the JSON data to a file
output_file_path = 'output.json'
with open(output_file_path, 'w') as output_file:
    output_file.write(json_string)

print(f"JSON data saved to: {output_file_path}")
