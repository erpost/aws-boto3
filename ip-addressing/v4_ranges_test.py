import v4_ranges as v4r

service_list = v4r.get_service_list()

for service in service_list:
    print(service)
print('\n')

selection = input('Select the Service you would like from the list above: ')

ip_ranges, count = v4r.get_ranges(selection)

if selection.upper() not in service_list:
    print('{} is not an available option. Exiting...'.format(selection))
else:

    print('\nThere are {0} ranges for {1} are:\n'.format(count, selection.upper()))

    for ip_range in ip_ranges:
        print(ip_range)
