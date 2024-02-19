import requests
import json

def update_record(input_new_rec_update, input_thing_to_update):
    # Get the list of DNS records
    email = "EMAIL"
    api_key = "API_KEY"
    zone_id = "ZONE_ID"

    record_type = "A"  # Change this to the type of record you want to update

    headers = {
        "X-Auth-Email": email,
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=headers)
    records = response.json()['result']

    # Find the specific record to update
    record_id = None
    for record in records:
        if record["name"] == input_new_rec_update and record["type"] == record_type:
            record_id = record["id"]
            break

    # Update the record with the new IP address
    if record_id:
        update_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
        data = {
            "type": record_type,
            "name": input_new_rec_update,
            "content": input_thing_to_update
        }
        update_response = requests.put(update_url, headers=headers, data=json.dumps(data))

        if update_response.status_code == 200:
            print(f"DNS record updated successfully: {input_new_rec_update} ({record_type}) to {new_ip}")
        else:
            print("Failed to update DNS record.")
    else:
        print("DNS record not found.")

public_ip = requests.get("https://api.ipify.org").text

# DNS record detail

new_ip = public_ip  # New IP address to set

with open("/root/ddns.conf", 'r') as ddns_conf:
    data = [line.strip() for line in ddns_conf]
    for item in data:
        print(item)
        update_record(str(item), public_ip)
