def dbQueryError(message, status=400):
    return [
        {
            'message': message,
            'status': status
        }
    ]

