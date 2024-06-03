import pynetbox

nb = pynetbox.api(
    'https://demo.netbox.dev/',
    token='c28971c1f00703ef03c3a63a8b84ab28b710dac3',
    threading=True,
)
devices = nb.dcim.devices.filter(role="router")
for device in devices:
    print(f"name: {device.name}, model: {device.device_type}")

print("##"*80)
def create_device(name: str, site: str, role: str, model: str) -> int:
    site_id = nb.dcim.sites.get(name=site)
    device_role = nb.dcim.device_roles.get(name=role)
    device_type = nb.dcim.device_types.get(model=model)
    if nb.dcim.devices.get(name=name) is not None:
        print(f"устройство с именем {name=} уже существует")
        return 0
    if site_id is None:
        print("Сайта не существует")
        return 0
    if device_role is None:
        print("Роль не существует")
        return 0
    result = nb.dcim.devices.create(
        name = name,
        device_type=device_type.id,
        site = site_id.id,
        role = device_role.id
    )
    if result:
        print("устройство создано")
        return result.id

print(create_device("dmi01-buffalo-rtr02", "DM-Camden", "Router", "ISR 1111-8P"))