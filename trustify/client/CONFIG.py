# Apache server root directory
SERVER_ROOT = "/etc/apache2/"
# Configuration file directory for trustify
CONFIG_DIR = "/etc/trustify/"
# Working directory for trustify
WORK_DIR = "/var/lib/trustify/"
# Directory where configuration backups are stored
BACKUP_DIR = WORK_DIR + "backups/"
# Replaces MODIFIED_FILES, directory where temp checkpoint is created
TEMP_CHECKPOINT_DIR = WORK_DIR + "temp_checkpoint/"
# Directory used before a permanent checkpoint is finalized
IN_PROGRESS_DIR = BACKUP_DIR + "IN_PROGRESS/"
# Where all keys should be stored
KEY_DIR = SERVER_ROOT + "ssl/"
# Certificate storage
CERT_DIR = SERVER_ROOT + "certs/"

# Used by openssl to sign challenge certificate with trustify extension
CHOC_CERT_CONF = CONFIG_DIR + "choc_cert_extensions.cnf"
# Contains standard Apache SSL directives
OPTIONS_SSL_CONF = CONFIG_DIR + "options-ssl.conf"
# Temporary file for challenge virtual hosts
APACHE_CHALLENGE_CONF = CONFIG_DIR + "choc_sni_cert_challenge.conf"

# Byte size of S and Nonce
S_SIZE = 32
NONCE_SIZE = 32

# bits of hashcash to generate
difficulty = 23 

# Trustify cert and chain files
cert_file = CERT_DIR + "trustify-cert.pem"
chain_file = CERT_DIR + "trustify-chain.pem"

# Rewrite rule arguments used for redirections to https vhost
REWRITE_HTTPS_ARGS = ["^.*$", "https://%{SERVER_NAME}%{REQUEST_URI}", "[L,R=permanent]"]
