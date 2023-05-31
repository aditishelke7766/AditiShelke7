import requests

url = 'https://www.ogb.state.ms.us/Downloads/WellInfoList/20230525_All_WellInfoList.csv'
save_path = r'C:\Users\ashelke3\OneDrive - Schlumberger\Rigs And Wells\PBI\Product Backlog Item 3760705 Ingestion of Gov Websites providing Well Data/API.csv'
read_path = r'C:\Users\ashelke3\OneDrive - Schlumberger\Rigs And Wells\PBI\Product Backlog Item 3760705 Ingestion of Gov Websites providing Well Data\API TXT.txt'

response = requests.get(url)

'''
## Data downloading and saving in local files
if response.status_code == 200:
    with open(save_path, 'wb') as file:         # wb -- opens a file from Save_path in write mode
        file.write(response.content)
    print("Excel sheet downloaded successfully.")
else:
    print("Failed to download the Excel sheet.")
'''


## data reading from local files
with open(read_path, 'r') as file:         # wb -- opens a file from Save_path in write mode
    data = file.read()
print(data)






    
