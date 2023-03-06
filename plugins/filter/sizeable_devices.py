#!/usr/bin/python


def shortname(dev):
    if dev.startswith('/'):
        return dev.split('/')[-1]
    return dev


def discover_volumes(facts, min_size, root_drive):
    devices = all_sizable_devices(facts)
    min_size = int(min_size)
    return [x for x in devices if x['size'] >= min_size and shortname(x["name"]) != shortname(root_drive)]


def all_sizable_devices(facts):
    devices = facts['devices']
    return [x for x in [{
        "name": name,
        "size": int(entry['sectors']) * int(entry['sectorsize']),
        "partitions": [p for p in entry['partitions']]
    } for name, entry in devices.items() if 'sectorsize' in entry]
    if x['size'] > 0]


def discover_mounts(facts, device):
    device = shortname(device)
    partitions = set(facts['devices'][device]['partitions'].keys())
    partitions.add(device)

    return [ { "device": entry["device"], "mount": entry["mount"]} for entry in facts['mounts'] if shortname(entry['device']) in partitions]


class FilterModule(object):
    ''' Collection of partitions/volumes discovery filters '''

    def filters(self):
        return {
            'discover_volumes': discover_volumes,
            'all_sizable_devices': all_sizable_devices,
            'discover_mounts': discover_mounts
        }
