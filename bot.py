# First load telegram and database modules
import source.modules.telegram as tg
import source.modules.database as db

# Select database file
db.database_init('./database.db')

# Init users package
import source.modules.users
source.modules.users.users_init()

# Init preferences package
import source.modules.preferences
source.modules.preferences.preferences_init()

# Import all commands
import source.modules.command_help
import source.modules.command_start

# Init all commands
source.modules.command_help.command_help_init()
source.modules.command_start.command_start_init()

# Start telegram loop
tg.run_polling()