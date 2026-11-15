# Creator: Astro_Age
# "In case someone else has this problem, here's a script that'll list materials off (replace "used_with_skeletal_mesh" with whatever flag you're looking for)"
# 
# TODO: Sp - Figure out where to organize this to, maybe a separate scripting section??

import unreal

reg = unreal.AssetRegistryHelpers.get_asset_registry()

regfilter = unreal.ARFilter(
    package_paths=[unreal.Name("/Game")],
    class_paths=[unreal.TopLevelAssetPath("/Script/Engine", "Material")],
    recursive_paths=True
)

assets = reg.get_assets(regfilter)
for assetdata in assets:
    mat = unreal.AssetRegistryHelpers.get_asset(assetdata)
    if mat and mat.get_editor_property("used_with_skeletal_mesh"):
        unreal.log(mat.get_path_name())