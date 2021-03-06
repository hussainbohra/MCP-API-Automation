import os

# MYSQL
MYSQL_HOST = os.environ.get('MYSQL_HOST', "mcp_db")
MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', "root")
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', "limpid@123")
MYSQL_DB = "mcp"

# Postgres
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', "mcp_db_pg")
POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', "limpid")
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', "limpid@123")
POSTGRES_DB = "mcp"


# Blue Planet Configuration

# Path Map
PATH_MAP = {
	'active_alarms' : ('/nsa/api/v1/alarms/filter/activeAlarms', 'data'),
	'device_types' : ('/nsa/api/v1/alarms/device-types', 'data'),
	'deviceAttributes' : ('/nsa/api/v1/alarms/deviceAttributes/{params}', 'data'),
	'networkConstructs' : ('/nsi/api/networkConstructs', 'data'),
	'tpes' : ('/nsi/api/tpes', 'data'),
	'fres' : ('/nsi/api/fres', 'data'),
	'physicalLocations' : ('/nsi/api/physicalLocations', 'data'),
	'equipment' : ('/nsi/api/equipment', 'data'),
	'managementSessions' : ('/discovery/api/managementSessions', 'data'),
	'HeatDissipationReport' : ('/equipmenttopologyplanning/api/v1/HeatDissipationReport', 'sites'),
	'policyTypes' : ('/commissioning/api/v1/policyTypes/', 'data'),
	'policy' : ('/commissioning/api/v1/policy/', 'data'),
	'policyDefaults' : ('/commissioning/api/v1/policyDefaults/', 'data'),
	'equipment_v4' : ('/nsi/api/v4/equipment', 'data'),
	'relationships' : ('/bpocore/market/api/v1/relationships', 'items'),
	'resource_types' : ('/bpocore/market/api/v1/resource-types', 'items'),
	'products' : ('/bpocore/market/api/v1/products', 'items'),
	'channelmargin' : ('/perfg/api/v1/channelmargin', 'services'),
	'config_templates' : ('/pm/api/v1/configs', 'data'),
	'nodes' : ('/pm/api/v1/nodes', 'data'),
	'resource_profiles' : ('/pmprocessor/api/v1/resource_profiles', 'data'),
	# These three seems to be a POST request, we might need to provide additional params
	'services' : ('/commissiong/api/v1/services', 'data'),
	'ipsubnet' : ('/commissioning/api/v1/ipsubnet/', 'shelfIP'),
	'scripts' :  ('/commissioning/api/v1/scripts/', 'data')
}

# Column Mapping for data transformation and data storage
COLUMN_MAP = {
	'active_alarms' : {
		'id' : ['id'],
	 	'type' : ['type'],
	 	'attributes_id' : ['attributes', 'id'],
	 	'attributes_node_id' : ['attributes', 'node-id'],
	 	'attributes_node_type' : ['attributes', 'node-type'],
	 	'attributes_resource' : ['attributes', 'resource'],
	 	'attributes_native_condition_type' : ['attributes', 'native-condition-type'],
	 	'attributes_condition_severity' : ['attributes', 'condition-severity'],
	 	'attributes_manual_clearable' : ['attributes', 'manual-clearable'],
	 	'attributes_additional_text' : ['attributes', 'additional-text'],
	 	'attributes_first_raise_time' : ['attributes', 'first-raise-time'],
	 	'attributes_last_raise_time' : ['attributes', 'last-raise-time'],
	 	'attributes_number_of_occurrences' : ['attributes', 'number-of-occurrences'],
	 	'attributes_acknowledge_state' : ['attributes', 'acknowledge-state'],
	 	'attributes_device_name' : ['attributes', 'device-name'],
	 	'attributes_ip_address' : ['attributes', 'ip-address'],
	 	'attributes_mac_address' : ['attributes', 'mac-address'],
	},
	'device_types' : {
		'id' : ['id'],
		'type' : ['type'],
		'attributes_id' : ['attributes', 'id'],
		'attributes_value' : ['attributes', 'value']
	},
	'equipment' : {
		'id' : ['id'],
		'type' : ['type'],
		'attributes_category' : ['attributes', 'category'],
		'attributes_nativeName' : ['attributes', 'nativeName'],
		'attributes_provisionedSpec_hardwareVersion' : ['attributes', 'provisionedSpec', 'hardwareVersion'],
		'attributes_locations_managementType' : ['attributes', 'locations', 'managementType']
	}
}
