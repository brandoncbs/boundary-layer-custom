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
        'boundary_layer',
        'enum34>=1.1.6,<2.0',
        'semver>=2.7.0,<3.0',
        'jsonschema>=2.6.0,<3.0',
        'jinja2>=2.8.1,<3.0',
        'pyyaml>=4.2b1',
        'marshmallow>=2.13.6,<3.0',
        'networkx>=2.1,<2.3',
        'xmltodict>=0.11.0,<1.0',
        'six>=1.11.0,<2.0',
    ]
)