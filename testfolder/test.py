import os
import socket
import ssl


def tls_version_check(ip_address, port):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection(address=(ip_address, port), timeout=120) as sock:
        with context.wrap_socket(sock, server_hostname=ip_address) as ssock:
            # The return value is a string with 'TLSv1.3' depending on the tls version.
            return ssock.version()


print(tls_version_check("102.162.200.10", 443))