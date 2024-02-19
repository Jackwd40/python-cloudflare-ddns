# Cloudflare Dynamic DNS (DDNS) Script

This script is designed to update the DNS records of your Cloudflare-managed domains dynamically using the Cloudflare API. It reads domain information from a configuration file (`ddns.conf`) and updates the DNS records one domain at a time.

## Installation

To use this script, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine.

2. **Install Required Packages:** Ensure you have the necessary packages installed. You can find the required packages in the header of the script.

3. **Create Configuration File:** Create a configuration file named `ddns.conf` in the root directory. This file should contain the necessary information for each domain you want to update. The format should be as follows:

    ```conf
        a.domain.com
        b.domain.com
        c.domain.com
    ```

4. **Update config:** Update the config information in the top few lines of the script. 

4. **Run the Script:** Execute the script, and it will read the configuration file, update each domain's DNS records with the current public IP address.

## Usage

Once you have set up the configuration file and installed the required packages, you can run the script using:

```bash
python cloudflare_ddns.py
