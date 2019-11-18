import setuptools

setuptools.setup(
    name = 'boundary_layer_custom',
    version='1.0.0',
    packages = setuptools.find_packages(),

    package_data = {
        'boundary_layer': [
            'builders/templates/*.j2',
            ],
        'boundary_layer_custom': [
            'config/generators/*.yaml',
            'config/operators/*.yaml',
            'config/resources/*.yaml',
            'config/subdags/*.yaml',
            ]
        },

    entry_points = {
            'boundary_layer_plugins': [
                'custom=boundary_layer_custom.plugin:CustomPlugin',
            ]
        },

    install_requires = [
        'boundary_layer'
    ]
)