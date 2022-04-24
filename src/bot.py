from aiogram import executor

import sys
from pathlib import Path
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv(Path().resolve().parent / '.env')

    if len(sys.argv) == 1:
        import handlers
        from misc import dp
        executor.start_polling(dp, skip_updates=True)
    elif sys.argv[1] == 'migrate':
        from models import City, User
        from misc import db
        db.create_tables([City, User, User.cities.get_through_model()])
        print('Successfully migrated')

