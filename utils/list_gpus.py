import torch

def count_print_devices():
    device_count = torch.cuda.device_count()
    print('{} devices found'.format(device_count))

    for device in range(device_count):
        print('Device {}: {}'.format(device, torch.cuda.get_device_name(device)))
    
    return device_count

if __name__ == '__main__':
    count_print_devices()

