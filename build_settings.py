
#-----------------------------------------------------------------------
# Node.js settings
#-----------------------------------------------------------------------
NODE_VERSION_MAJOR, NODE_VERSION_MINOR, NODE_VERSION_PATCH = 7, 4, 0

#-----------------------------------------------------------------------
# J2V8 settings
#-----------------------------------------------------------------------
J2V8_VERSION_MAJOR, J2V8_VERSION_MINOR, J2V8_VERSION_PATCH = 4, 7, 0

#-----------------------------------------------------------------------
# Combined & computed values
#-----------------------------------------------------------------------
NODE_VERSION = '{}.{}.{}'.format(NODE_VERSION_MAJOR, NODE_VERSION_MINOR, NODE_VERSION_PATCH)
J2V8_VERSION = '{}.{}.{}'.format(J2V8_VERSION_MAJOR, J2V8_VERSION_MINOR, J2V8_VERSION_PATCH)
