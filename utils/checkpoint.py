import json
import os

def save_afrinic_asn_checkpoint(processed_asn, processed_list, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    result = {
        "processed_asn": processed_asn,
        "processed_list": processed_list
    }

    with open(output_file, 'w') as f:
        json.dump(result, f)
    
    print(f"Checkpoint saved to {output_file}")

def save_ip_validator_checkpoint(valid_ip_addresses, invalid_ip_addresses, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    result = {
        "num_of_ip_addresses": len(valid_ip_addresses) + len(invalid_ip_addresses),
        "num_of_valid_ip_addresses": len(valid_ip_addresses),
        "num_of_invalid_ip_addresses": len(invalid_ip_addresses),
        "valid_ip_addresses": valid_ip_addresses,
        "invalid_ip_addresses": invalid_ip_addresses
    }

    with open(output_file, 'w') as f:
        json.dump(result, f)
    
    print(f"Checkpoint saved to {output_file}")

def save_tls_filterer_checkpoint(tls_1_3, tls_1_2, old_tls, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    result = {
        "tls_1_3": tls_1_3,
        "tls_1_2": tls_1_2,
        "old_tls": old_tls
    }

    with open(output_file, 'w') as f:
        json.dump(result, f)
    
    print(f"Checkpoint saved to {output_file}")


def save_tldr_checkpoint(processed_ip, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    num_of_ip_addresses = sum(len(processed_ip[key]) for key in processed_ip)
    results= {
        "num_of_ip_addresses": num_of_ip_addresses, 
        "ip_addresses_encoding": processed_ip,
    }
    
    with open(output_file, 'w') as f:
        json.dump(results, f)
    
    print(f"Checkpoint tldr saved to {output_file}.\n")
        