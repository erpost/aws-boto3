import requests

url = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
jurl = url.json()


def get_service_list():
    """get list of available services, without duplicates"""
    fcn_services = []
    fcn_aws_service_list = []

    for k in jurl['prefixes']:
        fcn_services.append(k['service'])

    for fcn_service in fcn_services:
        if fcn_service in fcn_aws_service_list:
            continue
        else:
            fcn_aws_service_list.append(fcn_service)

    return fcn_aws_service_list


def get_ranges(service_selection):
    """get IP ranges for specified service"""
    fcn_ip_ranges = []
    fcn_count = 0

    for k in jurl['prefixes']:
        if k['service'] == service_selection.upper():
            fcn_ip_ranges.append(k['ip_prefix'])
            fcn_count += 1

    return fcn_ip_ranges, fcn_count


if __name__ == "__main__":

    service_list = get_service_list()

    for service in service_list:
        print(service)

    print('\n')

    selection = 'CODEBUILD'
    ip_ranges, count = get_ranges(selection)

    for ip_range in ip_ranges:
        print(ip_range)

    print('\n{} ranges returned'.format(count))
