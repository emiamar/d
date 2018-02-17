from django.contrib.auth.models import Group, Permission

GroupsDict = {
    'admin': ['add_jobcard', 'add_reelmaterial', 'add_customer', 'add_vendor'],
    'operator': ['add_pyproduction'],
    'driver': ['add_dispatch']
}


def create_groups():
    for key, value in GroupsDict.items():
        g = Group.objects.get_or_create(name=key)
        for permission in value:
            g[0].permissions.add(
                Permission.objects.get(codename=permission)
            )
            g[0].save()
