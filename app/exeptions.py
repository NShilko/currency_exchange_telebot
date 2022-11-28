import texts


class ErrNoResponse(Exception):
    def __init__(self):
        print(texts.err_no_response)


class ErrUserWrongInput(Exception):
    def __init__(self, err):
        print(err)


class ErrWrongCurrency(Exception):
    def __init__(self, err):
        print(err)


class ErrWrongValue(Exception):
    def __init__(self, err):
        print(err)
