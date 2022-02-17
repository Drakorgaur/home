def log_user(user):
    return '[user]:\n' \
           f'\tusername: {user.username}\n' \
           f'\temail: {user.email}\n' \
           f'\t[room]:\n' \
           f'\t\tname: {user.room.name}\n'