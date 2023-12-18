# Copyright 2021,2023 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
def uninstall_hook(env):
    access = env.ref(
        "base.access_ir_module_module_group_user", raise_if_not_found=False
    )
    access.write({"active": True})
