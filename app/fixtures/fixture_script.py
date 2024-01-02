import json
try:
    json_file_path = 'comments.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
        for comment in data['comments']:
            new_comment = {
                "model": "app.comment",
                "pk": comment["id"],
                "fields": comment
            }
            # Replace the current comment with the new structure
            data['comments'][data['comments'].index(comment)] = new_comment
        data = data["comments"]
    with open(json_file_path, 'w') as json_file:
    # Write the modified data back to the file
        json.dump(data, json_file, indent=2)
except FileNotFoundError:
    print(f'File not found: {json_file_path}')
except json.JSONDecodeError:
    print(f'Error decoding JSON in {json_file_path}')
except Exception as e:
    print(f'An error occurred: {str(e)}')